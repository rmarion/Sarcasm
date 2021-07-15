import argparse
import random


def change_character_casing(character):
    if random.choice((True, False)):
        return character.upper()
    return character.lower()


# This is very fast and reasonably memory efficient, but is completely random (and as a result may not look 'random' enough)
def change_phrase_casing(phrase):
    return ''.join([change_character_casing(character) for character in phrase])


def change_file_casing(read_path, write_path=None):
    if not write_path:
        write_path = './output.txt'
    with open(read_path, 'r') as read_file:
        with open(write_path, 'w') as write_file:
            for line in read_file:
                write_file.write(change_phrase_casing(line))
    return change_phrase_casing('Successfully changed casing for {0}, saved to {1}'.format(read_path, write_path))


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