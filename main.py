from stats import *
import sys

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1] # Path to the book file
    book_text = get_book_text(book_path)
    
    num_words = word_count(book_text)  # Count the words in the book text
    
    chars = char_count(book_text)

    char_list = sort_char_count(chars)

    print(f"""============ BOOKBOT ============\n
Analyzing book found at {book_path}...\n
----------- Word Count ----------\n
Found {num_words} total words\n
--------- Character Count -------
""")
    for item in char_list:
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

    # Print the book text
    # print(book_text)

main()
