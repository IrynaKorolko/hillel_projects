def popular_words(text: str, words: list) -> dict:
    """The function counts hpw many times the "word" is found in the given text.

    Args:
        text (str): The text in which to count the words.
        words (list): A list of words to be counted in the text.
    Returns:
        dict: A dictionary with words(as keys) and their values (as counts).
    """
    our_dictionary = {}
    text_lower = text.lower()
    words_in_text = text_lower.split()
    for word in words:
        count = words_in_text.count(word)
        our_dictionary[word] = count
    return our_dictionary