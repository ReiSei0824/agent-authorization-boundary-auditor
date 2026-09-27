import unittest
from audit_authorization import audit

class AuditTests(unittest.TestCase):
    def test_bounded_read_goes(self):
        self.assertEqual(audit([{"action":"READ","scope":"tenant:42/tickets"}])["status"], "GO")
    def test_external_needs_gate(self):
        self.assertEqual(audit([{"action":"EXTERNAL_EXECUTION","scope":"mail:customer:42","approval":False}])["status"], "GO_WITH_GATES")
    def test_external_approved_goes(self):
        self.assertEqual(audit([{"action":"EXTERNAL_EXECUTION","scope":"mail:customer:42","approval":True}])["status"], "GO")
    def test_missing_scope_blocks(self):
        self.assertEqual(audit([{"action":"READ"}])["status"], "NO_GO")
    def test_unknown_blocks(self):
        self.assertEqual(audit([{"action":"DELETE_ALL","scope":"prod"}])["status"], "NO_GO")

if __name__ == "__main__": unittest.main()
