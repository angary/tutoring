from reverse import reverse_words

def test_empty_list():
    assert reverse_words([]) == []

def test_empty_strings():
    assert reverse_words([""]) == [""]

def test_single_word():
    assert reverse_words(["hello"]) == ["hello"]

def test_multiple_words():
    assert reverse_words(["Hello World"]) == ["World Hello"]

def test_multiple_strings():
    assert reverse_words(["Hello World", "I am here"]) == ["World Hello", "here am I"]

