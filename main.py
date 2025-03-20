from stats import get_num_words, count_characters, print_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        wordCount = get_num_words(text)
        characters = count_characters(text)
        print(print_report(filepath,wordCount,characters))
main()
