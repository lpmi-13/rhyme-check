import unittest
from rhyme_check.find_all_rhymes import find_all_rhymes
DATA_SOURCE = './data/sample.txt'

class FindAllRhymes(unittest.TestCase):

    def test_find_all_rhymes(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.readlines()
            cleaned = [line.strip() for line in data]
        expected = ['snow', 'go', 'slow', 'know', 'though', 'low']
        result = find_all_rhymes(cleaned)
        self.assertEqual(expected, result)        
