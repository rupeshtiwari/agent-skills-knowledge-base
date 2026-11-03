# Acceptance-Gate Demonstration

This educational gate checks that all declared requirements have a passed result and that evidence identifies the current artifact and contract bytes. It rejects missing, duplicate, unknown, failed or malformed results and stale hashes.

Run tests from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

To apply it to your own fixture:

```bash
python3 scripts/acceptance_gate.py artifact.txt contract.json evidence.json
```

A contract is an object with a nonempty `required_checks` array of unique string IDs. Evidence contains `artifact_sha256`, `contract_sha256`, and a `results` array. Each result has `id`, `status`, `validator`, and `evidence_location`. The only accepted status is `passed`. Hashes use the exact file bytes, including whitespace. See the test fixture for a complete programmatic example.

Exit code 0 means internal consistency passed; exit code 1 means HOLD. This command does not publish anything, execute validators, inspect evidence locations, authenticate evidence, or evaluate semantic correctness. An untrusted producer can fabricate a consistent evidence record. For production, bind trusted validator execution to the action boundary and prevent alternate publishing paths from bypassing it.

The included tests demonstrate the gate's bounded behavior. They do not establish that a model follows a skill or that the referenced checks are truthful. The `test_fabricated_evidence_limitation` case explicitly records this limit.
