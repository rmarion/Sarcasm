import unittest

from importlib import import_module
import_module('sarcasmscores')
from sarcasmscores import get_sarcasm_words_and_scores, parse_sarcasm_scores, get_score_for_phrase

class SarcasticTests(unittest.TestCase):

    def test_parses_words_and_scores_correctly(self):
        text = ['a, 1\n', 'b, 2\n','c, 3']
        parsed_scores = parse_sarcasm_scores(text)
        expected_scores = { 'a': 1, 'b': 2, 'c': 3 }
        for key in expected_scores.keys():
            self.assertEqual(parsed_scores[key], expected_scores[key])


    def test_reads_file_and_parses_correctly(self):
        (parsed_scores, _) = get_sarcasm_words_and_scores('test-sarcasm-scores.csv')
        expected_scores = { 'a': 1, 'b': 2, 'c': 3 }
        for key in expected_scores.keys():
            self.assertEqual(parsed_scores[key], expected_scores[key])


    def test_given_gets_correct_score_for_phrase_with_scored_word(self):
        (parsed_scores, parsed_words) = get_sarcasm_words_and_scores('test-sarcasm-scores.csv')
        test_phrases = { 'a test' : 1, 'b test' : 2, 'c test' : 3 }
        for phrase in test_phrases:
            self.assertEqual(get_score_for_phrase(phrase, parsed_scores, parsed_words), test_phrases[phrase])

        compound_test_phrases = { 'ab test' : 3, 'bc test' : 5, 'cc test' : 3 }
        for phrase in compound_test_phrases:
            self.assertEqual(get_score_for_phrase(phrase, parsed_scores, parsed_words), compound_test_phrases[phrase])


if __name__ == '__main__':
    unittest.main()
