def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is
    reversed
    '''
    result = []
    for string in string_list:
        words = string.split()
        wordsReversed = reversed(words)
        stringReversed = " ".join(wordsReversed)
        result.append(stringReversed)
    return result


if __name__ == "__main__":
    print(reverse_words(["Hello World", "I am here"]))
    # it should print ['World Hello', 'here am I']
