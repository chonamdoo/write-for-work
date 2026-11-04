# Plain language for work writing

## Contents

1. Decision rule
2. Korean sentence repair
3. Korean punctuation and spacing
4. Register and sentence endings
5. Matching a reference document
6. Imported workplace jargon
7. Stock Korean AI expressions
8. Vague action words
9. English AI expressions
10. Structural habits
11. Examples
12. Adaptation sources

## Decision rule

Do not ban a word only because AI often uses it. Change it when a more familiar and precise expression fits the reader.

1. Keep a formal identifier, product name, metric, API field, contractual term, or established specialist term.
2. Explain a necessary specialist term at first use for a mixed or non-technical audience.
3. Replace internal jargon when the reader can understand the same point more quickly in ordinary language.
4. Choose the replacement from the actual meaning in context. Do not apply a fixed synonym mechanically.
5. Remove the expression if it adds tone or weight but no information.

Examples of terms to preserve:

- Registered metric names and other formal identifiers
- API, HTTP, GPU, MAU, and ARPPU when technically required
- Legal and contractual wording whose exact form matters
- Product features and interface labels

Explain an acronym at first use when the reader may not know it.

Treat metaphor-derived words by their use, not their origin. Keep technical uses such as "테스트 격리", "배포 승격", and "파생 상태" when they name the actual operation or concept; explain them when the reader needs it. Replace a figurative use only when a concrete expression makes its meaning clearer.

When explaining a technical or quantitative concept, preserve the defining relationship, direction, and limits, not just its name. A familiar neighboring concept is not an equivalent definition. If a simplification introduces a definition or mechanism, ground it in supplied or verified material. Without that grounding, retain the original term and explain the supported result or limitation instead of adding a plausible definition or analogy.

For example, a linear relationship is a straight-line relationship; it can slope upward or downward and need not pass through zero. When explaining "선형 관계", "직선으로 나타낼 수 있는 관계" preserves that scope. A constant ratio between the values or a requirement that both increase together is narrower. Apply this distinction to the meaning, not as a ban on the word "비율".

## Korean sentence repair

Build the sentence around who does what, under which condition, rather than translating English word order or replacing isolated words. Name an actor only when the source identifies one; a passive is valid when the actor is unknown or irrelevant.

These are synthetic examples, not mandatory substitutions:

| Draft | Possible revision | Preserve |
|---|---|---|
| 설정 변경 작업을 수행한다 | 설정을 바꾼다 | The actual action; do not invent a new effect |
| 요청에 있어서 검증의 수행이 필요하다 | 요청을 검증해야 한다 | The requirement, not a claim that validation already happens |
| 응답이 수신되어진다 | 응답을 받는다 | Who receives it; retain passive wording if that actor is unknown |
| 오류가 발생할 수 있을 것으로 보인다 | 오류가 발생할 수 있다 | Uncertainty; never shorten this to "오류가 발생한다" |
| 승인이 없는 경우에는 배포가 허용되지 않는다 | 승인 없이는 배포할 수 없다 | The negative condition and prohibition |
| 새 엔진을 통하여 조회한다 | 새 엔진으로 조회한다 | The means; keep "통해" when it names a real channel or intermediary |
| 기존 화면 대비 필터 구성이 상이하다 | 필터 구성이 기존 화면과 다르다 | The comparison target and direction |
| 핵심이라 할 수 있다 | 핵심이다 | Only when the source supports the stronger claim; otherwise keep the hedge |
| 확인하시어 회신을 부탁드립니다 | 확인하신 뒤 회신을 부탁드립니다 | The `~습니다` register and politeness; replace only the stiff written connective `-시어`. `~해 주세요` would be a register change |

- Unpack noun chains into a subject and predicate when that clarifies the relationship. Keep an established noun such as "의존성 주입" rather than paraphrasing away its meaning. Keep each number, frequency, period, condition, and owner attached to the word it modifies in the source. If it can modify either of two words and the supplied context does not settle which, as `주 1회` in "검수 결과는 주 1회 품질 보고서에 반영됨" (reflected once a week, or a weekly report), keep its position; do not resolve it into "주 1회 작성하는 품질 보고서". Flag both readings only when the difference matters to the reader.
- Use one name for one concept. Do not alternate "사용자", "고객", and "클라이언트" for rhythm when they mean the same thing, or collapse them when they mean different things.
- Resolve the scope of `만/도/는` and negation from context before rewriting. "모두 승인하지 않았다" can mean none approved or not all approved; if the source does not settle the difference, flag both readings rather than choosing one.
- Give `이`, `그`, `해당`, and `이를` an unambiguous referent. Repeat the concrete noun or name the relevant event when several antecedents are possible; keep a clear pronoun, and do not invent a referent for an ambiguous source.
- Distinguish real identifiers from decorative English. Keep an exact token such as `retryCount`, but remove duplicate labels such as "retry 재시도" when `retry` is not an identifier. Explain unfamiliar terminology once for the intended audience.
- Keep the document's chosen register consistent. Technical instructions may repeatedly end in "~한다"; vary wording only when it improves comprehension, not to satisfy a rhythm rule.
- Read the Korean around code tokens on its own. Repair awkward particles or word order without translating the tokens.
- Preserve meaningful contrasts, necessary passive voice, real lists of three, and caution in legal or safety text. None is an error merely because a model also uses it.

## Korean punctuation and spacing

These marks often signal translated or machine-styled Korean work prose. Particle spacing (한글 맞춤법 제41항) and spaces around a middle dot (부록 문장 부호 5. 가운뎃점 해설: 가운뎃점은 앞말과 뒷말에 붙여 쓴다) are norm issues; the other rows are style heuristics that the norm does not forbid. Review each one in the passage being edited and revise it unless one of the keep cases below applies.

| Signal | Revise to |
|---|---|
| An em dash `—` that inserts an aside in a Korean sentence | A pair of commas, a colon, parentheses, or a separate sentence |
| A spaced middle dot ` · ` separating ordinary list items | Commas, or a slash in compact labels |
| Decorative `★`, emoji, or check marks used for emphasis | Delete; use the document's existing emphasis if emphasis is needed |
| `÷`, `=`, or `×` standing in for a word inside a prose sentence | Words such as "~로 나눈 값", "~은/는" |
| A space between Latin text, a number, a closing quote, or a code span and the particle or copula after it, such as `React 와`, `40,000 은`, `"제시" 에`, `` `maxRetry` 를 ``, `PoC 입니다` | Attach the particle: `React와`, `40,000은`, `"제시"에`, `` `maxRetry`를 ``, `PoC입니다` |
| Doubled spaces used as separators, or curly and straight quotes mixed in one document | One separator; the document's existing quote style |

Keep these:

- A middle dot joining paired or grouped terms, such as `성능·품질`, `회원·비회원`, `결측·이상값`, or groups inside a comma-separated list. Under the 맞춤법 punctuation rules it is written without spaces, so when a spaced dot joins such a pair, remove the spaces and keep the dot. A single spaced dot separating two attributes of one item, such as `No.12 · 시범 운영`, may also be kept; this is a style exception adapted from stop-slop-ko, not a norm rule.
- An em dash around an aside that itself contains a comma (required by 부록 문장 부호 쉼표 (13) [붙임 2]), before a subtitle, or where the source or reference document uses it consistently. A paired dash around a comma-free aside is also permitted (쉼표 (13) [붙임 1]), so replacing it is a style choice; do not call it an error.
- A dash or `—` in a table cell, `※` notes, and `→` or `▶` in flows and diagrams. A table dash can mean "not applicable", "none", or "not yet"; flag it when the meaning matters and the table does not define it. Flag `※` only when it is overused.
- Emoji that carries product meaning or matches a requested voice, and math notation that is the content, such as `1920×1080`, `3×`, a KPI formula, or `n = 30`.
- Every character inside code, commands, error text, identifiers, URLs, quoted source text, and formal names, even when it is one of the signals above.
- The space before a noun or a bound noun. Particles, including the copula `이다`, attach; nouns and bound nouns keep their space: `` `maxRetry` 값 ``, `API 서버`, `1시간 만에`, and `할 수 있다`. A unit noun after an Arabic numeral may attach (`3회`, `12,000건`; 제43항 다만); keep the source's choice.

These are revision checks for the edited passage, not a house-style ban; see [style-and-integrity.md](style-and-integrity.md#house-style-restrictions).

## Register and sentence endings

A Korean register is the ending class an element uses: 개조식 noun or `~함`/`~임`/`~됨` endings, plain `~다`, polite `~습니다`, or `~요`. Korean work documents legitimately use all of them. 개조식 appears in bullets, tables, minutes, and slides, and also in the body paragraphs of design documents and reports. No ending class is a sign of machine writing.

- When polishing, de-slopping, or making text "natural" (다듬기, AI 티 빼기, 자연스럽게) without asking for another form, keep each element's register. Advice to write active, short, direct sentences shortens a sentence's content, not its ending: `정의함` stays `정의함`, a `~습니다` post stays `~습니다`, and 개조식 bullets stay bullets.
- Change the register when the request or the reader requires it: the user names a register or asks to turn bullets or 개조식 into sentences (문장으로, 줄글로, 서술형으로, or 풀어서 together with such a target, as in 문장으로 풀어서), even when the request also says 자연스럽게; the destination template or a supplied reference sets one; Restructure or Draft produces a different format (an email from 개조식 notes); or the source register is wrong for its reader. 쉽게 풀어서 or 용어를 풀어서 alone asks for plainer words and keeps the register. Keep requirement strength and deadlines.
- A command addressed to the people who must act, such as `~할 것` or `철저를 기할 것` in a notice, request, or message, is a tone problem, not a register to keep. Polishing rewrites it in the artifact for internal and external readers alike; do not leave the polite form only as an alternative. Match the surrounding sentences: in `~습니다` text use `~해 주시기 바랍니다`, or `~해야 합니다` for a safety or compliance duty; in `~요` text use `~하세요` or `~해 주세요`; in plain `~다` text use `~해야 한다`; inside a 개조식 list or table whose other items stay 개조식, use `~해야 함`. When every sentence of a notice or message is such a command, use the `~습니다` forms. Keep `반드시`, deadlines, and whether the action is required or only permitted; do not soften a requirement into `가능하시면` or `편하실 때`, and do not add a penalty the source does not state. Keep the wording when the user asks to, when it is quoted, when a supplied reference or destination template uses it, and in statutes, regulations, contracts, RFP requirement lists, and code comments where `~할 것` is the established requirement form. Checklist items and minutes that record a requirement or decision in noun form, such as `증빙 제출 완료`, keep it; a `~할 것` action item in them follows the 개조식 form above (`~해야 함`).
- Repairing a predicate that does not fit its subject, such as "목표는 … 줄입니다" becoming "목표는 … 줄이는 것입니다", fixes grammar within the register and is not a register change.
- If the source already mixes registers within one element type, keep them unless the user asked to unify them. This needs no note unless the mix leaves the meaning ambiguous.
- When drafting without a template, prior edition, or sample, a common default is 개조식 for reports, minutes, tables, and slides, and `~합니다` for emails and notices.
- A list of three requirements, a contrast that corrects a real misconception, and a necessary passive in a specification are content. English anti-AI rules against groups of three or "not X but Y" do not apply to them.

## Matching a reference document

When asked to match another chapter, an approved document, or an author's style, take the signature from the unedited reference and apply it element by element: the draft's headings follow the reference headings, its notes follow the reference notes, and so on. One document can end headings in nouns and notes in `~함`.

Compare these features:

| Feature | What to observe |
|---|---|
| Endings | Separately for headings, bullets, notes, table cells, and body text |
| Punctuation | Dash, middle dot, parentheses, colon, quote style, spacing inside brackets |
| List separators | Commas, slashes, `>`, numbering, or line breaks |
| Particle density | Terse noun phrases or complete sentences with particles |
| Terms | English spelling or Korean transliteration, attached spelling, parenthetical glosses |
| Length and rhythm | One-line items or multi-clause sentences; for prose, paragraph length, first person, and how often paragraphs open with a connector |

Matching changes form, not content: keep every fact, number, condition, and requirement strength from the draft. Apply the punctuation and spacing checks above to the draft, except where the reference itself consistently uses a mark; then follow the reference without adding a note. An explicit user or destination punctuation requirement takes priority over the reference's convention; protect verbatim text, code, identifiers, and URLs as described in [House-style restrictions](style-and-integrity.md#house-style-restrictions). Matching means writing like the reference author, not making the draft more direct than the reference.

## Imported workplace jargon

| Signal | Prefer, depending on meaning |
|---|---|
| 게이트 | 판단 기준, 승인 조건, 검증 단계, 다음 검토 |
| 레버 | 바꿀 수 있는 요인, 조정 수단, 개선 방법, 비용 절감 방법 |
| 슬롯 | 항목, 입력란, 확인할 수치, 배정 시간 |
| 액션 아이템 | 할 일, 후속 작업, 다음 조치 |
| 얼라인, 얼라인먼트 | 합의하다, 방향을 맞추다, 기준을 통일하다 |
| 오너십 | 담당 책임, 책임 범위, 주도권 |
| 임팩트 | 영향, 효과, 결과, 변화 |
| 인사이트 | 발견, 해석, 확인한 점, 판단 근거 |
| 러닝 | 배운 점, 확인한 사실, 실험 결과 |
| 컨텍스트 | 배경, 맥락, 전제, 앞선 논의 |
| 내러티브 | 설명 흐름, 주장, 이야기 구조 |
| 프레임워크 | 기준, 구조, 분석 틀, 절차 |
| 로드맵 | 추진 계획, 단계별 계획, 일정 |
| 마일스톤 | 주요 일정, 중간 목표, 완료 기준 |
| 팔로업 | 후속 확인, 다음 작업, 추가 연락 |
| 브레이크다운 | 세부 내역, 항목별 구분, 나눠 보기 |
| 드라이브하다 | 추진하다, 주도하다, 진행하다 |
| 셋업 | 설정, 준비, 구성, 설치 |
| 킥오프 | 시작 회의, 착수, 작업 시작 |
| 어젠다 | 안건, 논의할 내용 |
| 디펜던시 | 선행 조건, 의존 관계, 먼저 필요한 작업 |
| 블로커 | 막힌 문제, 진행을 막는 요인 |
| 리소스 | 인력, 예산, 시간, 장비처럼 실제 대상을 명시 |
| 스코프 | 범위, 대상, 포함할 일 |
| 싱크 | 공유, 상태 확인, 내용 맞추기 |
| 롤아웃 | 순차 적용, 단계적 출시, 배포 |
| 랜딩 | 확정, 반영, 적용, 도착처럼 실제 의미를 명시 |
| 트랙 | 작업 흐름, 진행 경로, 추적 대상 |
| 베이스라인 | 비교 기준, 기본값, 기존 측정값 |
| 페인 포인트 | 불편, 문제, 막히는 지점 |
| 밸류 프로포지션 | 고객이 얻는 가치, 선택 이유 |
| 터치포인트 | 접점, 만나는 화면, 연락 시점 |
| 엔드투엔드 | 처음부터 끝까지, 전체 과정 |
| 유즈 케이스 | 사용 사례, 이용 상황 |
| 디시전 | 결정, 판단 |
| 테이크어웨이 | 결론, 기억할 내용, 핵심 결과 |

Some borrowed terms have several legitimate meanings. For example, do not replace "랜딩 페이지" with "확정 페이지". Interpret the phrase before editing it.

## Stock Korean AI expressions

Treat these as signals that the sentence may be adding weight without information.

| Signal | Check or rewrite |
|---|---|
| 단순한 X를 넘어 Y | State Y directly. Keep the contrast only if X and Y genuinely differ. |
| X에 그치지 않고 Y | State the additional result and its evidence. |
| X가 아니라 Y다 | Keep only when correcting a real misconception. |
| 흔히 ~라고 생각하기 쉽지만, 언뜻 ~가 나아 보이지만 | Apply the objection rule in [SKILL.md](../SKILL.md): distinguish sourced opposition from an explicitly hypothetical alternative. |
| 핵심은 명확하다 | State the actual conclusion. |
| 결국 중요한 것은 | Remove the lead-in and state what matters. |
| 결국 이게 핵심이다, 차이는 여기서 갈린다 | Remove a repeated section-ending slogan unless it adds a supported consequence or action. |
| 이러한 맥락에서 | Name the relationship or remove the transition. |
| 이를 통해 | State who did what and what changed. |
| 나아가 | Use only when the next point is a real extension. |
| 한편 | Use only for a genuine contrast or parallel point. |
| 종합적으로 볼 때 | State the conclusion and supporting evidence. |
| 주목할 만하다 | State the result that deserves attention. |
| 시사하는 바가 크다 | State the decision or next test the result supports. |
| 의미가 있다 | Explain what changes because of it. |
| 새로운 가능성을 열다 | Name the new capability, customer, or action. |
| 중요한 전환점 | Name what changed before and after. |
| 패러다임 전환 | Describe the operating or market change. |
| 게임 체인저 | Name the measurable advantage or remove it. |
| 새로운 여정을 시작하다 | State the work that begins. |
| 생태계를 구축하다 | Name the participants, exchange, and operating model. |
| 지속 가능한 성장 | Name the revenue, cost, retention, or operating condition. |
| 미래지향적 | Name the future requirement the choice satisfies. |
| 혁신적, 획기적 | Provide the observable difference or remove the praise. |
| 차별화된 | State the exact difference and comparison target. |
| 다층적, 다각적, 전방위적 | List the actual dimensions when they matter. |
| 선제적으로 | State what was done before which event or risk. |
| 체계적으로 | State the procedure, owner, or sequence. |
| 성공적으로 | State the completion or measured result. |
| 효과적으로 | State the effect and its measure. |
| 원활하게 | State what completed without which problem. |
| 본질적으로 | State the actual mechanism or definition. |
| 무엇보다 | Keep only when a real priority order exists. |
| 빠르게 변화하는 환경에서, ~하는 시대다, 그 어느 때보다 | Name the specific change and its evidence or date, or open with a concrete case. |
| 본 보고서에서는 ~을 알아보고자 한다, 이상으로 ~을 살펴보았다 | Open with the main finding and end with the conclusion instead of announcing the recap. |

Do not replace one empty abstraction with another. "시사하는 바가 크다" should not automatically become "중요한 인사이트를 제공한다".

### In paragraph prose

These signals apply to paragraph prose such as blog posts, essays, columns, and narrative retrospectives. They are judgment calls, not deletions to apply everywhere.

| Signal | Check or rewrite | Keep when |
|---|---|---|
| 정말, 매우, 굉장히, 진정한 | Remove, or replace with a number the source already supplies. | It is a scale value or label, such as "영향도: 매우 높음" or "매우 만족 42%". |
| Repeated ~라고 생각한다, ~라고 생각된다, ~라는 생각이 든다, ~라고 본다 | State directly what the source supports. | The claim is the author's opinion or unproven, especially a causal claim. |
| ~의 중요성을 깨달았다, ~라는 교훈을 얻었다 as an ending | End with the changed behavior or fact the source already states. If the source states none, delete the sentence or ask; do not supply one. | The sentence states a specific lesson the text supports, as in a retrospective's "배운 점". |
| 앞으로 ~하는 사람이 되겠다, ~해야 할 때다, 우리 모두의 과제다 as an ending | End with the source's concrete next action or open question, or on the last factual paragraph. | It is a real commitment with an action, owner, or date, such as "앞으로 매주 금요일에 공유하겠습니다". |
| An opening quotation, proverb, or dictionary definition | Open with the situation, fact, or claim. | The quote is the subject, such as an error message in an incident report, or the definition is what the document documents. |
| 오늘은 ~에 대해 알아보겠습니다, 그럼 시작해 볼까요?, 도움이 되셨길 바랍니다 | Start with the content. A replacement sentence that announces the topic, such as "~ 두 가지를 소개합니다", is the same opener. | A greeting or sign-off is part of a required template or the user's voice. |

## Vague action words

These words are useful only when the document names what changes.

| Signal | Make it concrete |
|---|---|
| 강화 | What becomes stronger, by which action, and how will it be measured? |
| 고도화 | Is accuracy improving, scope expanding, or work becoming automated? |
| 최적화 | Which metric improves under which constraint? |
| 효율화 | Does time, cost, error, or staffing decrease? |
| 극대화 | What is the target and current value? |
| 제고 | Does awareness, quality, conversion, or speed increase? |
| 확보 | What was obtained, in what amount, and is it confirmed? |
| 지원 | What action can the recipient now complete? |
| 연계 | Which systems, teams, or steps connect and how? |
| 활용 | Who uses what for which task? |
| 추진 | What work starts, who owns it, and by when? |
| 검토 | What decision will the review produce? |
| 대응 | What specific action addresses which risk? |

Examples:

- "운영 효율을 강화한다" becomes "수동 검수 시간을 줄인다" when that is the actual goal.
- "서비스를 고도화한다" becomes "고객 문의의 평균 처리 시간을 줄인다" when response time is the target.
- "데이터를 활용한다" becomes "지난 30일 결제 데이터를 가격 실험 대상 선정에 사용한다" when the source supports it.

## English AI expressions

| Signal | Prefer |
|---|---|
| In today's rapidly evolving landscape | Name the specific current change. |
| At its core | State the definition or mechanism directly. |
| It is important to note that | State the fact. |
| This underscores or highlights | State what the evidence shows. |
| Delve into | Examine, explain, or omit the framing. |
| Leverage | Use, apply, or name the exact action. |
| Foster | Build, increase, support, or name the mechanism. |
| Robust | State the tested capacity, reliability, or coverage. |
| Seamless | State the steps removed or failure rate measured. |
| Holistic | Name the included dimensions. |
| Unlock potential | Name the new action or measurable benefit. |
| Navigate complexity | Name the decision or difficulty. |
| Pivotal, transformative, groundbreaking | State the observable change. |
| A testament to | State the evidence without praise. |
| Not only X but also Y | State Y directly unless the contrast matters. |
| From X to Y | Use only when X and Y form a real range or sequence. |
| Moving forward | State the next action and the date the source gives; do not add a date. |
| In conclusion | End with the conclusion itself. |
| Poised to | State the condition required or use a sourced forecast. |

## Structural habits

Check for patterns that make writing look generated even when individual sentences are correct.

- Every section begins with a slogan-like question.
- Every paragraph has the same length and cadence.
- Ideas are repeatedly grouped into three without a content reason.
- Every bullet uses a bold label followed by one generic sentence.
- The introduction announces the document instead of giving the answer.
- The conclusion repeats the introduction without a decision or next action.
- Every section adds a closing slogan that repeats its last fact.
- Prose repeatedly breaks into noun fragments such as "근거 없음. 대안 없음." Combine related fragments into a sentence when that clarifies the relationship. Keep 개조식 sentences ending in `~함` or `~됨`, bullets, table cells, status labels, and fragments the author uses deliberately.
- Headings, cards, callouts, and highlights all emphasize the same point.
- Unknowns are hidden under "추후 검토" without stating what decision they affect.
- The document alternates between inflated claims and broad disclaimers.
- A social post opens with manufactured controversy or ends with engagement bait.

Keep useful structure. Remove only the structure that decorates or simulates analysis.

## Examples

### Business report

Supplied context for this synthetic example: the next review concerns cost reduction and follow-up work.

Before:

> 다음 게이트에서 핵심 레버와 액션 아이템을 얼라인한다.

After:

> 다음 검토에서 비용을 줄일 방법과 후속 작업을 합의한다.

### Quantitative input

Before:

> 사업성 판단을 위한 정량 슬롯을 채운다.

After:

> 사업성 판단에 필요한 수치를 채운다.

Keep the action: filling in values is not finalizing or approving them.

### AI-style conclusion

Supplied facts for this synthetic example: a new approval procedure passed an internal test; its effect on processing time has not been measured in a pilot.

Before:

> 이러한 맥락에서 이번 결과는 단순한 기술 검증을 넘어 사업의 새로운 가능성을 연다는 점에서 의미가 있다.

After:

> 새 결재 절차는 내부 시험을 통과했다. 실제 처리 시간이 줄어드는지는 시범 운영에서 확인해야 한다.

### Formal identifier

Before:

> `PAYMENT_STATUS`는 API 응답에 정의된 필드다.

After:

> `PAYMENT_STATUS`는 API 응답에 정의된 필드다.

Keep the identifier because changing it would damage precision.

### Missing evidence

Before:

> 처리 효율을 개선할 수 있을 것으로 보인다.

After:

> 처리 효율이 나아질 수 있다.

The source supplies no affected step or measurement. Do not turn this into "검수 시간을 30% 줄인다". If the document needs that detail, report the missing evidence outside the revised passage.

## Adaptation sources

The Korean and technical-writing additions were authored for this skill after reviewing these sources on 2026-09-12:

- [im-not-ai rewriting playbook](https://github.com/epoko77-ai/im-not-ai/blob/main/skills/humanize-korean/references/rewriting-playbook.md): Korean translationese, register, and modality preservation.
- [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md): source-fact and non-prose protection; figurative jargon versus real technical usage.
- [Humanizer KR](https://github.com/hjongc/humanizer-kr/blob/main/skills/humanizer-kr/SKILL.md): audience-aware Korean and minimal revision.
- [Patina technical documents](https://github.com/devswha/patina/blob/main/document-types/technical.md) and [code comments](https://github.com/devswha/patina/blob/main/document-types/code-comment.md): document-specific constraints and exact technical meaning.

These are references, not runtime dependencies or proof of rewriting quality. The PR mode in [modes.md](modes.md) applies those principles to reviewable changes. Examples here are synthetic; no AI-authorship claims, forced change ratios, invented experiences, or external execution workflows are adopted.

The 2026-09-14 update uses [issue #2's adversarial review](https://github.com/chonamdoo/write-for-work/issues/2) as its supplied source for instruction clarity, evidence presentation, and document-purpose checks across this package. The referenced proposal was unavailable in the repository; its missing text was not reconstructed, and the issue's external-source attributions were not independently reverified. Exceptions for supported interpretation, clear pronouns, coupled actions, historical facts, real deadlines, and short mixed-purpose documents are this skill author's adaptations, not quoted source rules.

Subsequent 2026-09-14 source-grounded evaluation informed narrower safeguards for technical simplification, sender commitments, and output shape. The technical distinction draws on [ABS: Correlation and causation](https://www.abs.gov.au/statistics/understanding-statistics/statistical-terms-and-concepts/correlation-and-causation), including its linear-relationship limits; commitment and output-shape safeguards are author-derived repairs to this skill's existing source and task boundaries. These are not a requirement to load research records at runtime or a claim of general writing-quality improvement.

The 2026-11-03 update adapted Korean punctuation and spacing signals, register preservation, reference-document matching, and paragraph-prose clichés from [stop-slop-ko](https://github.com/leeandev/stop-slop-ko) (Copyright (c) 2026 leeandev, MIT License; commit `553be05`, reviewed 2026-11-03), mainly its `ko-slop-patterns.md`, `prose-patterns.md`, and `tone-extraction.md` references. The rules were rewritten for this skill; short example strings such as `"제시" 에`, `40,000 은`, `성능·품질`, and the blog greetings are reused from it. Its opinion rule was narrowed to fit this skill's evidence rules: an unsupported opinion is kept as a hedge instead of deleted or supported with added evidence, and its "keep only one opinion" limit was not adopted. Its prose clichés are limited here to paragraph prose with keep conditions for scale values, specific lessons, and real commitments. Its scanner script, hook, file-format editing recipes, and essay and cover-letter modes were not adopted. The punctuation and spacing keep cases follow 한글 맞춤법 ([text](https://korean.go.kr/kornorms/regltn/regltnView.do?regltn_code=0001&regltn_no=303), checked 2026-11-03): 제41항 for particles, 제42항 for bound nouns, and the 부록 문장 부호 rules for 줄표 and 가운뎃점.

The 2026-11-04 update repairs defects found by an adversarial review of this package and its 2026-11-03 evaluation outputs. The polite rewrite of reader-addressed commands follows 국립국어원, 『쉬운 공문서 쓰기 길잡이』 (2022), 21–23쪽, as summarized in this repository's research notes: for 대국민 documents it rewrites `~을 것` as `~어야 함` or `~하세요` and requests as `~해 주시기 바랍니다` without turning a duty into an option. The research notes add that it is no basis for rewriting noun-form decision records in internal minutes. Applying the rewrite to internal notices, the checklist exception, and the keep cases for statutes, contracts, RFPs, and code comments are this skill author's adaptations from evaluation case KP08 and its observed failure. 국립국어원, 『한눈에 알아보는 공공언어 바로 쓰기(개정판)』 (2022), 11–12쪽, and 법제처, 『알기 쉬운 법령 정비기준 제10판(수정증보판)』, 152–155쪽, ask writers to make a modifier's target clear; keeping an unresolved modifier in its source position is this skill's adaptation for editors who lack the writer's intent. Norm citations were rechecked against 한글 맞춤법 (시행 2017-03-28) at the same link on 2026-11-04: 제41항, 제43항 다만, 부록 문장 부호 쉼표 (13) [붙임 1–2], and the 가운뎃점 spacing note in its commentary. The note, Review-output, mode-priority, and two-way comparison rules are this skill author's repairs to conflicts between existing rules, not quoted source rules.
