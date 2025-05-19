def word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    num_words = len(text.split())
    return num_words

def char_count(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        char_log: The number of each character in the text.
    """
    text = text.lower()
    char_log = {}
    chars = list(text)
    for char in chars:
        if char in char_log:
            char_log[char] += 1
        else:
            char_log[char] = 1
    return char_log

def list_sorter (chars):
    return chars[1]
def sort_char_count(char_log):
    """
    Sorts the dictionary of characters made from char_count

    Args:
        char_log (dictionary): The count of each character in the text
    
    Returns:
        char_list: Sorted list of each character count in the text.
    """
    char_list = list(char_log.items())
    alpha_list = []
    for item in char_list:
        key = item[0]
        if key.isalpha():
            alpha_list.append(item)

    alpha_list.sort(reverse=True,key=list_sorter)
    return alpha_list