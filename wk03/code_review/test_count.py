from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_word():
    assert count_char("Deconstructed") == { "D": 1, "e": 2, "c": 2, "o": 1, "n": 1, "s": 1, "t": 2,
                                            "r": 1, "u": 1, "d": 1}

def test_sentence():
    assert count_char("A small sentence") == {  "A": 1, " ": 2, "s": 2, "m": 1, "a": 1, "l": 2, "e": 3,
                                                "n": 2, "t": 1, "c": 1}
