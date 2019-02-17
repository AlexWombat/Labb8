import unittest

from L08 import *


class SyntaxTest(unittest.TestCase):

    def teststorbokstav(self):
        """ Testar saknad stor bokstav """
        self.assertEqual(kollaMolekyl("aa"), "Saknad stor bokstav.")

    def testlitettal(self):
        """ Testar om något tal är mindre än 1 """
        self.assertEqual(kollaMolekyl('A1'), "För litet tal vid radslutet.")

    def korrektstorbokstav(self):
        """ Testar saknad stor bokstav """
        self.assertEqual(kollaMolekyl("Aa"), "Följer syntaxen!")

    def korrektstorttal(self):
        """ Testar om något tal är mindre än 1 """
        self.assertEqual(kollaMolekyl('A4'), "Följer syntaxen!")


if __name__ == '__main__':
    unittest.main()

