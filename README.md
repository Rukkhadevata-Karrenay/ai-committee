# AI Committee

English | [简体中文](README.zh-CN.md)

A role-based decision-review Skill for Codex. It splits a complex question across a coordinator, an independent proposer, an adversarial critic, a privacy reviewer, and a verifier, so the final result carries the proposal alongside counterexamples, assumptions, evidence gaps, risks, and a next verification step.

AI Committee works standalone for everyday work and does not depend on AI Memory. If an authorized memory context exists in the environment, it can be used as an optional input; a memory system, database, or other persistent store is never a prerequisite for installing or running it.

> AI Committee is not "let several models vote." Model opinions are advisory only — facts still need to be confirmed by first-party sources, actual tests, or other verifiable evidence.

## What problem it solves

A single model tends to converge quickly on an answer that looks reasonable, but complex decisions usually need more than that:

- Independent alternatives, not the same answer restated in different words;
- Active hunting for counterexamples, failure paths, and missing conditions;
- A clear line between verified facts, judgment, assumptions, and unknowns;
- A stated way to verify each recommendation, not just the recommendation itself;
- Scope limits on outbound data before calling external models, so private content isn't leaked unconditionally.

AI Committee turns these requirements into a repeatable role workflow and a unified output structure.

## When to use it

- System architecture, API design, data models, and technology choices;
- Complex project plans, migration strategies, and recovery designs;
- Review of high-value documents, product proposals, or research conclusions;
- Decisions that need independent proposals and adversarial critique;
- Tasks that need permission, privacy, concurrency, data-loss, or failure-recovery risks identified;
- Cases needing current public information, where browser reference models cross-check facts;
- You already lean toward an answer but want the committee to actively challenge it.

The following usually don't need a committee:

- A one-line command, a simple translation, or basic formatting;
- A single fact that can be checked directly;
- Routine file reads, hashing, permission checks, or duplicate-content checks;
- Routine operations with no meaningful trade-off.

## Core design

### 1. Decide whether a committee is worth forming at all

The Skill picks the smallest viable path based on the question's value, complexity, ambiguity, and risk:

```text
Simple, low risk
    → handled directly by a single model

Moderate complexity
    → one primary model + necessary structure/privacy checks

High value, with a clear trade-off or failure risk
    → independent proposal + adversarial critique + verified synthesis

Needs committee discussion or current public information
    → free web models preferred, after the privacy check

Question too complex for the free web path
    → high-capability web models before high-capability paid models
```

It never routes every question through every model just to look like a multi-agent system.

### 2. Each role works independently, then a single synthesis

| Role | Responsibility | Must not do |
|---|---|---|
| Coordinator | Clarify the question, narrow scope, pick the smallest sufficient member set | Hint at a single "correct" answer up front |
| Independent proposer | Propose without seeing other members' answers | Echo the coordinator's preference |
| Adversarial critic | Find counterexamples, missing evidence, edge cases, and failure modes | Invent risks just to object |
| Privacy reviewer | Check outbound content, sensitivity, and output structure | Widen the authorized scope |
| Verifier / Synthesizer | Reconcile opinions, preserve consensus, dissent, and unverified assumptions | Treat majority opinion as proof |

Independent proposals reduce false consensus caused by members echoing each other; the adversarial role catches cases where everyone answered from the same unquestioned premise; the verifier grounds the final recommendation in an executable test.

### 3. No simple majority vote

Multiple models can share training data, prompt bias, and false premises, so agreement doesn't mean correctness. The final synthesis must answer:

- What is backed by a source or a test;
- What is only model judgment;
- Which members disagreed, and why;
- What evidence is still missing;
- What the smallest next verification step is.

### 4. Elastic model routing

Committee discussion follows a "free first, escalate by capability" order:

1. Run the local privacy check first, reducing the question to the smallest public/internal package allowed to leave the machine;
2. Prefer free web models capable of the task, using the smallest sufficient member count;
3. For unusually complex questions, pick the currently strongest, best task-fit web model with benchmark evidence, rather than a fixed vendor;
4. Consider a high-capability paid model only when free web models are unavailable or proven insufficient;
5. A paid model requires explicit authorization, provider configuration, and budget already in place — never invoked automatically just because it "might be better."

So for complex questions, the capability order is:

```text
high-capability free web models
    > authorized high-capability paid models
    > an incomplete or unsupported forced synthesis
```

Local division of labor is preserved alongside this:

- Luna / medium: pre-filtering, structure checks, privacy checks, and simple diff extraction;
- Terra / medium: coordinates complex tasks and produces the final synthesis;
- "High-capability paid model" describes model capability and payment channel — it does not authorize Codex to use high/max reasoning;
- Never silently substituted with Sol, high, or max;
- An unavailable member is marked incomplete and the run degrades gracefully; it never blocks an ordinary single-model task.

Which models are actually available depends on the Codex environment running the Skill. This repository ships no model accounts, API keys, browser login state, or usage quota.

## Browser reference members

When a user explicitly invokes `$ai-committee` and the question can be reduced to non-sensitive public/internal content, that invocation already authorizes the committee to prefer available free web reference members without asking again per model. Logged-in Gemini, Qwen, DeepSeek, Kimi, GLM, or Doubao web sessions can all be candidates.

The actual priority among web models is decided dynamically by current availability, task type, and demonstrated capability — it is never a permanent vendor ranking. Sensitive, restricted, or local-operational content is never sent to web models just because free models are preferred.

Browser members are suited for:

- Looking up current public information;
- Independent planning;
- Cross-checking public facts;
- Critiquing an existing proposal.

Browser members are not a stable API and not an execution agent. They cannot read local files, run commands, modify code or databases, or act as the final authority. On login expiry, CAPTCHA, timeout, or a UI change, that member is marked unavailable and the local flow continues.

## Installation

### Prerequisites

- Codex with Skills support installed;
- Git available locally;
- Reopen Codex after installing so the Skill directory is rediscovered.

### Windows PowerShell

```powershell
git clone https://github.com/Rukkhadevata-Karrenay/ai-committee.git `
  "$env:USERPROFILE\.codex\skills\ai-committee"
```

### macOS / Linux

```bash
git clone https://github.com/Rukkhadevata-Karrenay/ai-committee.git \
  "$HOME/.codex/skills/ai-committee"
```

### Updating

```powershell
git -C "$env:USERPROFILE\.codex\skills\ai-committee" pull --ff-only
```

## Usage

### Explicit invocation

```text
$ai-committee
Review this plan for me — give an independent proposal, counterarguments,
evidence needed, and a next verification step.
```

### Natural-language invocation

```text
Use AI Committee to compare these three approaches and keep the dissenting views.
```

### Recommended prompt template

```text
$ai-committee

Question: <the decision to review>
Goal: <what you want to achieve>
Known facts: <facts already verified>
Current leaning: <optional, lets the committee challenge it>
Hard constraints: <budget, time, platform, compatibility, etc.>
Public sources allowed: <optional>

Please output:
1. Independent alternative proposals;
2. Supporting reasons and counterarguments;
3. Unverified assumptions and the evidence needed;
4. Security or privacy risks;
5. A recommended approach and the smallest next verification step.
```

## Examples

### Technology choice

```text
$ai-committee
Compare SQLite, PostgreSQL, and an event-store service as the authority
for a local-first app. Focus on migration, concurrency, backup/recovery,
and operational cost.
```

### Plan review

```text
$ai-committee
Review this eight-week study plan. Find assumptions that won't hold up,
over-scheduling, and steps missing acceptance evidence; give a sturdier version.
```

### Challenging a current leaning

```text
$ai-committee
I lean toward option A. Have the independent proposer answer without
knowing that leaning, then have the adversarial critic focus on finding
failure scenarios for A.
```

### Needing current public information

```text
$ai-committee
This is a public, non-sensitive question. Browser reference members may
be used to check current official docs and version info; cite sources,
and list anything unverifiable separately.
```

## Output structure

The committee's recommendation follows this unified structure:

```json
{
  "proposal": {},
  "supporting_reasons": [],
  "counterarguments": [],
  "assumptions": [],
  "evidence_needed": [],
  "security_concerns": [],
  "dissenting_views": [],
  "confidence": 0.0,
  "recommended_next_test": []
}
```

| Field | Meaning |
|---|---|
| `proposal` | The final recommendation or candidate approach |
| `supporting_reasons` | Supporting reasons and their evidence status |
| `counterarguments` | The strongest objections and failure scenarios |
| `assumptions` | Premises the recommendation relies on but hasn't proven |
| `evidence_needed` | What's still needed before a reliable decision |
| `security_concerns` | Permission, privacy, data, and execution risks |
| `dissenting_views` | Disagreement not absorbed into the final recommendation |
| `confidence` | Subjective confidence from 0 to 1 — not a probability of fact |
| `recommended_next_test` | An executable next verification action |

Full spec: [output-schema.md](references/output-schema.md).

## Security and privacy boundaries

Content allowed to be sent to external reference members is limited to:

- A de-identified question;
- The smallest public/internal summary needed to complete the task;
- Anonymous space labels, source IDs, or content hashes;
- The allowed output structure.

Never sent:

- Sensitive/restricted content;
- Raw chat transcripts and Evidence quotes;
- Tokens, cookies, passwords, API keys, and account credentials;
- Local absolute paths and environment variables;
- Precise locations and private relationships;
- Medical, financial, or legal privacy;
- Unauthorized data spaces.

Model responses must also be treated as untrusted text — never executed directly as commands. Full rules: [security-policy.md](references/security-policy.md).

## Relationship to AI Memory

AI Committee could originally pair with AI Memory, but is now a standalone Skill:

- Without AI Memory: it uses the user's input and any permitted public evidence directly;
- With AI Memory: only authorized, filtered, and minimized context is used as input;
- The committee cannot write Memory Events, modify Projections, approve its own Proposals, merge memory across Spaces, or lower sensitivity;
- A committee recommendation entering long-term memory still goes through the normal Evidence, classification, conflict, and review pipeline.

## Failure and degradation behavior

- A member is unavailable: keep completed results, mark the missing role, never pretend the committee is complete;
- Browser login expires or a CAPTCHA appears: stop that member, fall back to local models;
- No reliable source available: lower confidence and list it under `evidence_needed`;
- Members repeat the same opinion: merge the duplicate wording but keep independent evidence and real disagreement;
- Sensitive content detected: block it from going out, handle it with a local single model or rules instead;
- The task turns out to be simple: complete it with a single model, no extra committee.

## Project structure

```text
ai-committee/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-policy.md
│  ├─ output-schema.md
│  └─ security-policy.md
├─ scripts/
│  └─ validate_committee_output.py
├─ README.md
└─ LICENSE
```

- `SKILL.md`: the core instructions Codex loads;
- `agents/openai.yaml`: interface name, default prompt, and invocation policy;
- `references/`: security, output, and benchmark rules loaded on demand;
- `scripts/validate_committee_output.py`: validates that structured output contains the required fields.

## Validating structured output

```powershell
Get-Content result.json | python scripts/validate_committee_output.py
```

On success:

```json
{"valid": true}
```

The script exits non-zero if fields are missing or `confidence` is outside 0 to 1.

## Development and self-check

After modifying the Skill, use Codex's built-in Skill validator to check the directory and frontmatter:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

Before committing, also check:

- Whether the name in `SKILL.md` is `ai-committee`;
- Whether `agents/openai.yaml`'s default prompt uses `$ai-committee`;
- Whether `references/` contains local paths, credentials, or private data;
- Whether the output validator's valid and invalid samples still behave as expected.

## Current boundaries

- This is a Codex Skill, not a standalone multi-model SaaS;
- The repository ships no external model accounts, API keys, usage credits, or browser login state;
- Web models are reference members, not guaranteed to stay available long-term;
- The committee never proves a conclusion correct by itself;
- The reliability of automatic triggering still needs ongoing evaluation against real task benchmarks;
- Final edits, publishing, database writes, and permission changes remain controlled by the executing agent and the user's authorization.

## License

[MIT License](LICENSE) © 2026 Karrenay
