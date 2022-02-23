def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    pass

'''
* What is a test list? Why is it important?
- Test list - a list of tests that cover the specification cases.
  Test lists are important as they are the basis for the correctness of the 
  system - anything that's left off the test list is a potential defect or bug 
  in the area that's not going to have a test written.




* What is a good approach to writing a test list?
- You always want to test edge cases
- You also always want to test success cases
- Say a strong password is a password that is at least 50 characters, it would
  be better to test that 49 characters is not a strong password, than testing
  48 or 30 characters is not a strong password
'''

def test_empty_string():
    assert(check_password("") == "Poor password")


def test_horrible_password():
    assert(check_password("password") == "Horrible password")
    assert(check_password("iloveyou") == "Horrible password")
    assert(check_password("123456") == "Horrible password")

# Num 1
def test_moderate_password_success():
    assert(check_password("abcdefgh1") == "Moderate password")


def test_moderate_password_8_chars_no_num():
    assert(check_password("abcdefgh") == "Poor password")


def test_moderate_password_7_chars_one_num():
    assert(check_password("abcdefg1") == "Poor password")

# Num 2
def test_moderate_password():
    assert(check_password("abcdefgh1") == "Moderate password")
    assert(check_password("abcdefgh") == "Poor password")
    assert(check_password("abcdefg1") == "Poor password")
