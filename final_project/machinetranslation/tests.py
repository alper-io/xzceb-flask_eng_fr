import unittest
from translator import english_to_french, french_to_english

class TestEnglishTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #test to check whether translation is true or not

class TestFrenchTranslator(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hi') #test to check whether translation is true or not
        
unittest.main()

        