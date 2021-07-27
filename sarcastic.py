import argparse
import random


def coinflip():
    return random.random() < 0.5


# A generator which returns random casing - the generator structure looks awkward, but it saves on memory, and we need to remember state
def get_random_casing(phrase, max_same_in_a_row):
    use_lower = coinflip()
    current_is_lower = False
    current_streak = 1
    for character in phrase:
        if use_lower:
            yield character.lower()
            current_is_lower = True
        else:
            yield character.upper()
            current_is_lower = False
        if current_streak < max_same_in_a_row:
            use_lower = coinflip()
            if use_lower == current_is_lower:
                current_streak += 1
        else:
            use_lower = not use_lower 
            current_streak = 1


def change_phrase_casing(phrase):
    return ''.join(get_random_casing(phrase, 3))


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