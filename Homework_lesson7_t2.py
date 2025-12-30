def correct_sentence(text):
    corrected_sentence = text.capitalize()
    result = corrected_sentence if corrected_sentence.endswith('.') else corrected_sentence + '.'
    return result