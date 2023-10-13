from nltk import download as ntlk_download
from nltk.corpus import wordnet as guru
from random import choice

class Synonymizer:
    def __init__(self):
        ntlk_download('wordnet')

    def replace_words(self, phrase, joiner, replacer_func):
        return joiner.join((replacer_func(word) for word in phrase.split()))

    def get_synonym(self, word):
        synonyms = guru.synonyms(word)
        synonyms = [synonym_list for synonym_list in synonyms if synonym_list]
        selected = choice(choice(synonyms))
        return selected if selected else word
    
    def synonymize(self, phrase, joiner):
        return self.replace_words(phrase, joiner, self.get_synonym)
