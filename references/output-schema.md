# Advisory output schema

```json
{"provider":"gemini-web","provider_type":"browser_reference_provider","role":"web_researcher","timestamp":"...","invocation_mode":"browser_assisted_evaluation","proposal":{},"recommendation":"...","supporting_reasons":[],"counterarguments":[],"web_findings":[{"claim":"...","source_url":"https://...","source_title":"...","source_date":"...","retrieved_at":"...","stale":false,"conflicts_with_local_evidence":false}],"assumptions":[],"evidence_needed":[],"security_concerns":[],"dissenting_views":[],"confidence":0.0,"recommended_next_test":[],"can_execute_locally":false,"memory_authority":false}
```

Model agreement is not factual verification. Preserve dissent and distinguish
source-backed facts, judgments and unresolved assumptions.
The local adapter stamps provider/type/role/time/mode and the two false
authority fields; never trust the webpage to set them. A citation is Advisory
Evidence only, not an automatically verified fact.
