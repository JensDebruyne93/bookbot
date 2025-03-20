def get_num_words(book_text):
    listOfWords = book_text.split()
    numberOfWords = len(listOfWords)
    return f"{numberOfWords} words found in the document"

def count_characters(book_text):
    character_dictionary = {}
    text_lower_case = book_text.lower()
    for char in text_lower_case:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary