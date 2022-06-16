import sys
sys.path.append('../')

import unittest
import translator

class TestingTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        # Test Hello -> Bonjour
        translation = translator.englishToFrench('Hello')
        self.assertEqual(translation, 'Bonjour')

        # Test null input
        translation_null = translator.englishToFrench(None)
        self.assertNotEqual(translation_null, None)

    def test_frenchToEnglish(self):
        # Test Bonjour -> Hello
        translation = translator.frenchToEnglish('Bonjour')
        self.assertEqual(translation, 'Hello')

        # Test null input
        translation_null = translator.frenchToEnglish(None)
        self.assertNotEqual(translation_null, None)

unittest.main()