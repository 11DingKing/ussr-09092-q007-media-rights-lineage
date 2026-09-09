import sys
import unittest
from datetime import datetime, timezone
sys.path.insert(0, "src")
from media_rights.domain import asset_ids, MediaRightsWindow

class DomainTest(unittest.TestCase):
    def test_first_occurrences(self):
        self.assertEqual(asset_ids([{"id":"a"}, {"id":"a"}, {"id":"b"}]), ["a", "b"])
    def test_reverse_time_rejected(self):
        window = MediaRightsWindow("x", datetime(2026, 1, 1, tzinfo=timezone.utc), datetime(2026, 1, 1, tzinfo=timezone.utc))
        with self.assertRaises(ValueError):
            window.duration_seconds()

if __name__ == "__main__":
    unittest.main()
