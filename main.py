def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = count_words(text)
    print(f"there are {num_words} words!")
    char_count = count_characters(text)
    print(char_count)

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
            #increment the counter integer by 1
            characters[char] += 1
        else: 
            #add the char to the characters dictionary as the key
            #then set the counter to 1
            characters[char] = 1
    return characters
main()