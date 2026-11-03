import copy
import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('gate', Path(__file__).resolve().parents[1] / 'scripts/acceptance_gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class GateTests(unittest.TestCase):
    def setUp(self):
        self.artifact = b'Example artifact'
        self.contract = json.dumps({'required_checks': ['R01', 'R02']}).encode()
        self.evidence = {'artifact_sha256': gate.digest(self.artifact), 'contract_sha256': gate.digest(self.contract),
                         'results': [{'id': k, 'status': 'passed', 'validator': 'demo-v1', 'evidence_location': 'example-log'} for k in ['R01', 'R02']]}

    def check(self, evidence=None, artifact=None, contract=None):
        return gate.assess(self.artifact if artifact is None else artifact,
                           self.contract if contract is None else contract,
                           self.evidence if evidence is None else evidence)

    def test_valid_consistency(self):
        self.assertEqual(self.check(), [])

    def test_stale_artifact(self):
        self.assertIn('Artifact hash mismatch', self.check(artifact=b'Changed'))

    def test_stale_contract(self):
        self.assertIn('Contract hash mismatch', self.check(contract=self.contract+b' '))

    def test_missing_check(self):
        self.evidence['results'].pop()
        self.assertIn('Missing check: R02', self.check())

    def test_duplicate_check(self):
        self.evidence['results'].append(copy.deepcopy(self.evidence['results'][0]))
        self.assertIn('Duplicate result: R01', self.check())

    def test_unknown_check(self):
        self.evidence['results'][0]['id'] = 'R99'
        self.assertIn('Unknown check: R99', self.check())

    def test_failed_blocked_unknown_states(self):
        for state in ['failed', 'blocked', 'not_run', None, True]:
            with self.subTest(state=state):
                self.evidence['results'][0]['status'] = state
                self.assertIn('Check not passed: R01', self.check())

    def test_empty_evidence_location(self):
        self.evidence['results'][0]['evidence_location'] = ' '
        self.assertIn('Missing evidence_location: R01', self.check())

    def test_malformed_results(self):
        self.evidence['results'] = 'passed'
        self.assertIn('Results must be a list', self.check())

    def test_empty_contract(self):
        self.assertTrue(self.check(contract=b'{"required_checks":[]}'))

    def test_duplicate_contract_ids(self):
        self.assertIn('Duplicate required check IDs', self.check(contract=b'{"required_checks":["R01","R01"]}'))

    def test_fabricated_evidence_limitation(self):
        # Demonstrates why this gate must not be presented as an authenticated validator.
        self.assertEqual(self.check(), [])

if __name__ == '__main__':
    unittest.main()
