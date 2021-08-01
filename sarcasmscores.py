def get_sarcasm_words_and_scores(path):
    try:
        with open(path, 'r') as sarcasm_file:
            scores = parse_sarcasm_scores(sarcasm_file.readlines())
            return (scores, set(scores.keys()))
    except: # Just return an empty collection if the list fails. We aren't running any telemetry for this, but if we do this should log a warning
        return ([], set([]))


def get_pair(pairtext):
    pair = pairtext.split(',')
    return (pair[0].lower(), int(pair[1]))


def parse_sarcasm_scores(lines):
    pairs = [get_pair(pairtext) for pairtext in lines]
    return dict(pairs) # Expecting (key: word, value: score) pairs from the sarcasm file


def get_score_for_phrase(phrase, sarcasm_scores, sarcasm_words):
    return sum([sarcasm_scores[word] for word in sarcasm_words if word in phrase.lower()])
