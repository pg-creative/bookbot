import sys

def get_book_text(filepath):
    """
    Read the contents of a file and return it as a string.
    
    Args:
        filepath (str): The path to the file to read
        
    Returns:
        str: The contents of the file as a string
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        return ""

from stats import count_words, count_characters, sort_characters

def main():
    """
    Main function that reads a book file and creates a beautiful report
    """
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line argument
    book_path = sys.argv[1]
    
    # Get the book text
    book_text = get_book_text(book_path)
    
    # Generate the report
    if book_text:
        # Count words
        num_words = count_words(book_text)
        
        # Count and sort characters
        char_count = count_characters(book_text)
        sorted_chars = sort_characters(char_count)
        
        # Print the beautiful report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        # Print only alphabetical characters
        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["num"]
            if char.isalpha():
                print(f"{char}: {count}")
        
        print("============= END ===============")
    else:
        print("Failed to read the book file.")

if __name__ == "__main__":
    main()
