"""String checks for tests/behavior/cases.json.

Each case maps acceptance indices to a check over the revised artifact only.
A criterion without a check is judged by reading; the evidence record keeps
that judgment and its reason. Checks prove only what a string can show.
"""

import re

NOTE_START = re.compile(r"^(-{3,}|\*\*|#+ |확인|참고|검토|메모|변경|수정)")


def _strip_fence(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else ""
        text = text.replace("```", "")
    return text.strip()


def _until_note(text):
    lines = []
    for line in text.splitlines():
        if lines and NOTE_START.match(line.strip()) and not line.startswith("##"):
            break
        lines.append(line)
    return "\n".join(lines).strip()


def artifact(case_id, output):
    """Return the revised artifact, excluding review notes after it."""
    text = _until_note(_strip_fence(output))
    lines = text.splitlines()
    if case_id.startswith("K1"):
        last = max((i for i, line in enumerate(lines) if line.startswith("|")), default=-1)
        return "\n".join(lines[: last + 1])
    if case_id.startswith(("K4", "K7", "K9")):
        keep = [i for i, line in enumerate(lines)
                if line.startswith(("- ", "#")) or (case_id.startswith("K4") and line.startswith("※"))]
        return "\n".join(lines[: keep[-1] + 1]) if keep else ""
    return text


def _sentences(text):
    text = re.sub(r"\[[^\]]*\]", "", text)
    lines = [l for l in text.splitlines() if not l.lstrip().startswith(("#", "**"))]
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", "\n".join(lines)) if re.search("[가-힣]", s)]


def _has(text, *needles):
    return all(n in text for n in needles)


def _gaejosik(text):
    return not re.search(r"(한다|된다|합니다|됩니다|했다|이다)\.?\s*$", text, re.M)


CHECKS = {
    "K1-gaejosik-deslop": {
        0: lambda a: _gaejosik(a),
        1: lambda a: "★" not in a and " · " not in a
        and all("—" not in l for l in a.splitlines() if not l.startswith("|")),
        2: lambda a: re.search(r"\|\s*오타 보정\s*\|\s*—\s*\|", a) is not None,
        3: lambda a: "성능·품질" in a,
        4: lambda a: _has(a, "12,000", "2.4초", "0.6초", "사내 시험 환경", "PostgreSQL에서"),
    },
    "K2-blog-prose": {
        0: lambda a: all(re.search(r"(니다|요)[.!?]?$", s) for s in _sentences(a)),
        2: lambda a: "깨달" not in a and "도움이 되셨" not in a,
        3: lambda a: not re.search(r"덕분입니다|덕분이었습니다|덕분에 롤백", a),
        4: lambda a: _has(a, "4회", "1회", "지난 분기") and ("두 명" in a or "2명" in a),
    },
    "K3-clean-spec": {
        0: lambda a: _has(a, "5회", "6회째", "30분", "12자", "대문자", "소문자", "숫자를 모두",
                         "승인으로만", "아니라", "※")
        and len(re.findall(r"다\.$", a, re.M)) >= 4,
    },
    "K4-tone-match": {
        0: lambda a: re.search(r"^###\s*4\.1 [^\n]*[^다.]$", a, re.M) is not None
        and not re.search(r"(다|니다)\.?\s*$", a, re.M),
        1: lambda a: "—" not in a and " · " not in a,
        2: lambda a: _has(a, "고객센터", "앱", "웹", "24시간", "원래 결제 수단", "부분 환불", "관리자 승인"),
    },
    "K5-pr-verbatim": {
        0: lambda a: _has(a, "`Retry limit — exceeded`", "`maxRetry`"),
        1: lambda a: not any(s in a for s in ("PR 을", "통하여", "개선을 진행", "` 가")),
        2: lambda a: "로컬에서만" in a and "통과" not in a,
    },
    "K6-gaejosik-body-natural": {
        0: lambda a: len(re.findall(r"(함|됨)\.", a)) >= 3
        and not re.search(r"(한다|된다|합니다|됩니다)\.", a),
        1: lambda a: _has(a, "5분", "3회", "별도 큐", "수동") and "생성" not in a
        and any(s in a for s in ("일 1회", "하루 1회", "하루 한 번")),
    },
    "K7-slide-symbols": {
        0: lambda a: " · " not in a and " = " not in a and "✅" not in a,
        1: lambda a: "회원·비회원" in a,
        2: lambda a: _has(a, "40%", "2주", "기대") and _gaejosik(a),
    },
    "K8-retro-keep": {
        0: lambda a: "매우 높음" in a,
        1: lambda a: _has(a, "금요일", "공유") and "매주" in a,
        2: lambda a: _has(a, "스테이징", "먼저"),
        3: lambda a: _has(a, "7월", "2시간", "운영 DB")
        and all(re.search(r"(니다|요)[.!?]?$", s) for s in _sentences(a)),
        4: lambda a: "정말 많은" not in a,
    },
    "K9-punct-keep": {
        0: lambda a: "1920×1080" in a,
        1: lambda a: "1시간 만에" in a,
        2: lambda a: _gaejosik(a),
        3: lambda a: "수집·정제" in a,
    },
    "KP02-regression": {},
    "KP03-regression": {},
    "KP08-regression": {},
}


def k7_note_separated(output):
    """K7 criterion 3: the first line after the slide bullets is not a bare ※ note."""
    lines = [l for l in _strip_fence(output).splitlines() if l.strip()]
    i = 0
    while i < len(lines) and lines[i].startswith("- "):
        i += 1
    return not (i < len(lines) and lines[i].startswith("※"))


def run(case_id, output):
    """Return {criterion_index: bool} for every mechanically checked criterion."""
    art = artifact(case_id, output)
    result = {i: bool(fn(art)) for i, fn in CHECKS[case_id].items()}
    if case_id == "K7-slide-symbols":
        result[3] = k7_note_separated(output)
    return result
