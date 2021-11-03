 # Copyright 2021 Accioma (https://accioma.com).
 # @author marcelomora <java.diablo@gmail.com>
 # License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import unittest
from ecedi import sequence

class TestSequence(unittest.TestCase):
    def test_sequence_valid(self):
        seq = "1-1-000000012"
        res = sequence.is_sequence_valid(seq)
        self.assertEqual(res, False)

        seq = "001-001-000000012"
        res = sequence.is_sequence_valid(seq)
        self.assertEqual(res, True)

    def test_next_sequence_valid(self):
        seq = "001-001-000000123"
        res = sequence.next_sequence(seq)
        self.assertEqual(res, "001-001-000000124")

    def test_from_simple(self):
        seq = "1-1-1"
        res = sequence.from_simple(seq)
        self.assertEqual(res, "001-001-000000001")

        seq = "001-001-000000009a"
        with self.assertRaises(ValueError):
            res = sequence.from_simple(seq)

if __name__ == '__manin__':
    unittest.main()
