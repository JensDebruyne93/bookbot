from stats import get_num_words, count_characters, print_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    wordCount = get_num_words(text)
    characters = count_characters(text)
    print(print_report(filepath,wordCount,characters))
main()
