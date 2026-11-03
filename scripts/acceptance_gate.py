#!/usr/bin/env python3
"""Educational consistency gate; supplied evidence is NOT authenticated."""
import argparse
import hashlib
import json
from pathlib import Path

def digest(data):
    return hashlib.sha256(data).hexdigest()

def assess(artifact, contract_bytes, evidence):
    errors = []
    contract = json.loads(contract_bytes)
    required = contract.get('required_checks')
    if not isinstance(required, list) or not required or any(not isinstance(x, str) or not x for x in required):
        return ['Contract must declare nonempty required_checks']
    if len(set(required)) != len(required):
        errors.append('Duplicate required check IDs')
    if evidence.get('artifact_sha256') != digest(artifact):
        errors.append('Artifact hash mismatch')
    if evidence.get('contract_sha256') != digest(contract_bytes):
        errors.append('Contract hash mismatch')
    results = evidence.get('results')
    if not isinstance(results, list):
        return errors + ['Results must be a list']
    seen = set()
    for result in results:
        if not isinstance(result, dict) or not isinstance(result.get('id'), str):
            errors.append('Malformed result')
            continue
        key = result['id']
        if key in seen:
            errors.append('Duplicate result: ' + key)
        seen.add(key)
        if key not in required:
            errors.append('Unknown check: ' + key)
        if result.get('status') != 'passed':
            errors.append('Check not passed: ' + key)
        for field in ('validator', 'evidence_location'):
            if not isinstance(result.get(field), str) or not result[field].strip():
                errors.append('Missing ' + field + ': ' + key)
    errors.extend('Missing check: ' + x for x in required if x not in seen)
    return errors

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('artifact', type=Path)
    p.add_argument('contract', type=Path)
    p.add_argument('evidence', type=Path)
    a = p.parse_args()
    try:
        evidence = json.loads(a.evidence.read_text())
        if not isinstance(evidence, dict):
            raise ValueError('Evidence must be an object')
        errors = assess(a.artifact.read_bytes(), a.contract.read_bytes(), evidence)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        errors = ['Invalid input: ' + str(exc)]
    print(json.dumps({'status': 'HOLD' if errors else 'CONSISTENCY_CHECK_PASSED', 'errors': errors,
                      'limitation': 'Evidence authenticity and semantic correctness are not verified.'}, indent=2))
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
