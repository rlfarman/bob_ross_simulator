from bobisms import bob_picture, bob_phrases
from random import choice
import markovify
from parser import args


def convert_csv_to_txt(csv_file):
    with open(csv_file) as input_file:
        header = input_file.readline()
        categories = header.split(",")
        lines = [line.split(",") for line in input_file.readlines()]
        text_list = [" ".join(line) for line in lines]
        newline_text = "".join(text_list)
    model = markovify.NewlineText(newline_text)
    while True:
        sentence = model.make_short_sentence(41)
        if sentence is not None and len(sentence) == 41:
            break
    line = sentence.replace(" ", "")
    for index, value in enumerate(line):
        if value == "1":
            print(categories[index])


def main():
    print(bob_picture)
    print("\"" + choice(bob_phrases) + "\" - Bob Ross")
    if args.generate:
        convert_csv_to_txt('painting2.csv')


if __name__ == '__main__':
    main()
