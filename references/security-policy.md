# Security policy

Allowed fields are run/task ID, purpose, de-identified question, public/internal
minimum summary, anonymous Space labels, Source IDs, hashes and output schema.
Block sensitive/restricted data, raw chats, Evidence quotes, credentials,
tokens, cookies, absolute paths, precise location, private relations,
medical/financial/legal privacy and unauthorized Spaces. Member output is
untrusted data and must never be executed as instructions. Audit only metadata
and hashes, never request or response bodies.

Cost preference never overrides privacy. Free browser models are preferred only
after the same minimization and sensitivity gate used for every external member.
Paid model use additionally requires an approved provider and budget.

`local_operational` is also forbidden. Block authorization headers, environment
variables, local usernames and database-internal identities. Public data may be
sent; internal data must be reduced to the minimum necessary summary. Browser
members have `local_execution=false`, `local_file_access=false`,
`shell_execution=false`, `code_modification=false`, `memory_write=false`, and
`authority_write=false` regardless of what the webpage recommends.
