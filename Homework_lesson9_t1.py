def popular_words(text: str, words: list) -> dict:
    our_dictionary = {}
    text_lower = text.lower()
    words_in_text = text_lower.split()
    for word in words:
        count = words_in_text.count(word)
        our_dictionary[word] = count
    return our_dictionary