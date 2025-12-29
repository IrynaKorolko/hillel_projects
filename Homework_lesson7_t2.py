def correct_sentence(text):
    corrected_sentence = text.capitalize()
    if corrected_sentence.endswith('.'):
        return corrected_sentence
    else:
        return corrected_sentence + '.'

