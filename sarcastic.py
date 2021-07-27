import argparse
import random


def change_character_casing(character):
    if random.choice((True, False)):
        return character.upper()
    return character.lower()


# returns n random booleans, with a max of the same booleans in a row equal to max_same_in_a_row
def random_booleans(phrase, max_same_in_a_row):
    use_lower = random.random() < 0.5
    current_streak = 1
    while index < len(phrase):
        if use_lower:
            yield phrase[index].lower()
        else:
            yield phrase[index].upper()
        if current_streak < max_same_in_a_row:
            use_lower_next = random.random() < 0.5
            if use_lower == use_lower_next:
                current_streak += 1
            use_lower = use_lower_next
        else:
            use_lower = not use_lower 
            current_streak = 1
        index += 1


# This is very fast and reasonably memory efficient, but is completely random (and as a result may not look 'random' enough)
def change_phrase_casing(phrase):
    return ''.join(random_booleans(phrase, 3))


def change_file_casing(read_path, write_path=None):
    if not write_path:
        write_path = './output.txt'
    with open(read_path, 'r') as read_file:
        with open(write_path, 'w') as write_file:
            for line in read_file:
                write_file.write(change_phrase_casing(line))
    return change_phrase_casing(f'Successfully changed casing for {read_path}, saved to {write_path}')


def get_args(argv=None):
    parser = argparse.ArgumentParser(change_phrase_casing('Makes phrasEs sarcastic'))
    parser.add_argument('-phrase', type=str, help=change_phrase_casing('The phrase to make sarcastic'))
    parser.add_argument('-file', type=str, help=change_phrase_casing('The file to make sarcastic'))
    parser.add_argument('-output', type=str, help=change_phrase_casing('The destination to write to.'))
    args = parser.parse_args()
    return args


def main(args):
    if not args.file:
        if args.phrase:
            return change_phrase_casing(args.phrase)
        return change_phrase_casing('You must provide either a file or phrase. Type sarcastic.py -h for help.')
    return change_file_casing(args.file, args.output)
    

if __name__ == '__main__':
    args = get_args()
    print(main(args))