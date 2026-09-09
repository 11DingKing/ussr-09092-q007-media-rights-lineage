import sys
import unittest
from datetime import date
sys.path.insert(0, "src")
from media_rights.rights import Right
from media_rights.lineage import ancestors

class RightsTest(unittest.TestCase):
    def test_withdrawal_blocks_use(self): self.assertFalse(Right("a", date(2026, 8, 1), True).active(date(2026, 7, 1)))
    def test_lineage_walks_to_source(self): self.assertEqual(ancestors("crop", {"crop":"photo", "photo":"raw"}), ["photo", "raw"])

if __name__ == "__main__": unittest.main()
