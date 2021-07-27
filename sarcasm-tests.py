import unittest

from importlib import import_module
import_module('sarcastic')
from sarcastic import change_phrase_casing

class SarcasticTests(unittest.TestCase):

    def test_max_three_of_same_casing_in_a_row(self):
        phrase = "a" * 1000
        sarcastic_phrase = change_phrase_casing(phrase)
        current_is_lower = sarcastic_phrase[0].islower()
        current_streak = 1
        for character in sarcastic_phrase[1:]:
            if character.islower() == current_is_lower:
                current_streak += 1
            else:
                current_streak = 1
                current_is_lower = not current_is_lower
            self.assertLess(current_streak, 4)

if __name__ == '__main__':
    unittest.main()