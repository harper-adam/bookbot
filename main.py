def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = word_count(text)
    num_letters = letter_count(text)
    sorted_letters = chars_dict_sorted_list(num_letters)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_letters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("--- End of report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(file_contents):
    words = len(file_contents.split())
    return words

def letter_count(text):
    lowered_string = text.lower()
    character_count = {}
    for letter in lowered_string:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1
    return character_count

def sort_on(d):
    return d["num"]

def chars_dict_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    
main()