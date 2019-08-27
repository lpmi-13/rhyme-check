import unittest
from ipa_conversion import convert_to_ipa


class CheckIPAConversionFunction(unittest.TestCase):

    def test_word_converts_to_IPA(self):
        word = 'boom'
        expected = convert_to_ipa(word)
        result = 'boom'
        self.assertEqual(expected, result)
