def get_num_words(book_text):
    listOfWords = book_text.split()
    numberOfWords = len(listOfWords)
    return numberOfWords

def count_characters(book_text):
    character_dictionary = {}
    text_lower_case = book_text.lower()
    for char in text_lower_case:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    print(character_dictionary)
    return character_dictionary

def sort_dict(dictionary):
    sorted_dictionary = sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
    return dict(sorted_dictionary)

def dict_to_text(dictionary):
    string = ""
    for key in dictionary:
        if key[0].isalpha():
            string += "\n" + f"{key[0]}: {dictionary[key]}"
    return string        

def print_report(text_path, number_of_words, character_dictionary):
    sorted_dict = sort_dict(character_dictionary)
    report_string = "============ BOOKBOT ============"
    report_string += "\n" + f"Analyzing book found at {text_path}..."
    report_string += "\n" + "----------- Word Count ----------"
    report_string += "\n" + f"Found {number_of_words} total words"
    report_string += "\n" + "--------- Character Count -------"
    report_string += dict_to_text(sorted_dict)
    report_string += "\n" + "============= END ==============="
    return report_string