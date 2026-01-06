def first_word(text) -> str:
    """Returns the first word in a given text string.
    Args:
        text: str
    Returns:
        str: the first word in the string
    """
    for char in text:
        if char == ' ' or char == ',' or char == '.':
            break
        if char.isalpha():
            start_index = text.index(char)
        for i in range(start_index, len(text)):
            if text[i] == ' ' or text[i] == ',' or text[i] == '.':
                end_index = i
            elif text[i] == "'":
                continue
        return text[start_index:end_index]
        
        



    