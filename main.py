def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    generate_report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    lowercase_text = text.lower()
    characters = {}

    for char in lowercase_text:
        if char in characters:
            characters[char] += 1
        elif char.isalpha(): 
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def convert_and_sort(characters):
    ordered = []
    for char, count in characters.items():
        ordered.append({
            "character": char,
            "count": count
        })
    ordered.sort(reverse=True, key=sort_on)
    return ordered



def generate_report(path, text):
    chars_by_count = convert_and_sort(count_characters(text))
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document")
    print("\n")
    
    #iterate through characters by count and print a nice f string for each
    for el in chars_by_count:
        print(f"The '{el['character']}' character was found {el['count']} times")
    print("--- End report ---")

main()