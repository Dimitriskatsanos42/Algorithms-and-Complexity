import unittest
from functions import brute_force, lcs, dp_table , dp_table


class MyTestCase(unittest.TestCase):
    def test_brute_force(self):
        seq1 = "AATCGAG"
        seq2 = "CCATCGG"
        self.assertEqual(brute_force(seq1, seq2), (5, "ATCGG"))

    
    def test_lcs(self):
        seq1 = "AATCGAG"
        seq2 = "CCATCGG"
        self.assertEqual(lcs(seq1, seq2), (5, "ATCGG"))

    
    def test_dp_table_list(self):
        self.assertEqual(
            dp_table("ABCDE", "CEFGH"),
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 2, 2, 2, 2],
            ],
        )


if __name__ == "__main__":
    unittest.main()