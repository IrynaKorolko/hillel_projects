def second_index (text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    else:
        second_index = text.find (some_str, first_index + len(some_str))
    return second_index




