"""src/main.py modulidagi salomlash() funksiyasi uchun unit testlar."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import salomlash  # noqa: E402


class SalomlashTestlari(unittest.TestCase):
    def test_oddiy_ism(self):
        self.assertEqual(salomlash("Gulruh"), "Assalomu alaykum, Gulruh!")

    def test_probellar_olib_tashlanadi(self):
        self.assertEqual(salomlash("  Ali  "), "Assalomu alaykum, Ali!")

    def test_bosh_ism_xato_beradi(self):
        with self.assertRaises(ValueError):
            salomlash("   ")


if __name__ == "__main__":
    unittest.main()
