import unittest
from translator import englishToFrench,frenchToEnglish
class test_tranlator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

unittest.main()
