def get_num_words(book_text):
    listOfWords = book_text.split()
    numberOfWords = len(listOfWords)
    return f"{numberOfWords} words found in the document"