def count_words(text):
    """
    Count the number of words in a string.
    
    Args:
        text (str): The text to count words in
        
    Returns:
        int: The number of words in the text
    """
    # Split the text into words and count them
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Count the frequency of each character in a string.
    
    Args:
        text (str): The text to count characters in
        
    Returns:
        dict: A dictionary with characters as keys and their counts as values
    """
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Convert text to lowercase and count each character
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_characters(char_count):
    """
    Sort character counts from greatest to least.
    
    Args:
        char_count (dict): Dictionary with characters as keys and counts as values
        
    Returns:
        list: A sorted list of dictionaries with character and count information
    """
    # Create a list of dictionaries with character and count
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list by count in descending order
    char_list.sort(reverse=True, key=lambda x: x["num"])
    
    return char_list