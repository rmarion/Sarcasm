import unittest

from importlib import import_module
import_module('synonymizer')
from synonymizer import Synonymizer

class SynonymTests(unittest.TestCase):

    def test_replaces_words_with_given_words(self):
        base_phrase = 'test phrase'
        joiner = ' '
        expected = 'result result'
        sut = Synonymizer()
        actual = sut.replace_words(base_phrase, joiner, lambda w: 'result')
        self.assertEquals(expected, actual)

    def test_finds_synonym_for_word(self):
        word = 'pant'
        sut = Synonymizer()
        synonym = sut.get_synonym(word)
        self.assertNotEqual(word, synonym)
        self.assertIsInstance(synonym, str)
        self.assertIsNotNone(word)

    def test_replaces_words_with_synonym(self):
        phrase = 'test phrase'
        joiner = ' '
        sut = Synonymizer()
        actual = sut.synonymize(phrase, joiner)
        self.assertNotEqual(phrase, actual)
        self.assertIsInstance(actual, str)
        self.assertIsNotNone(actual)

if __name__ == '__main__':
    unittest.main()
