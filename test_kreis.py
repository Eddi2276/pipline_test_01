import unittest

from kreis import kreis_flache
from math import pi

class TestKreisFlaeche(unittest.TestCase):
    def test_flaeche(self):
        #testes fläche wenn radius = 0
        self.assertAlmostEqual(kreis_flache(1),pi)
        self.assertAlmostEqual(kreis_flache(0),0)
        self.assertAlmostEqual(kreis_flache(2.1),pi* 2.1**2)
