def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(book_text):
    listOfWords = book_text.split()
    numberOfWords = len(listOfWords)
    return f"{numberOfWords} words found in the document"

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    wordCount = count_words(text)
    print(wordCount)

main()
