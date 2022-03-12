def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number,
      at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    if password in ('password', 'iloveyou', '123456'):
        return "Horrible password"
    if (len(password) >= 12 and any(x.isupper() for x in password) and
        any(x.isdigit() for x in password) and
        any(x.islower() for x in password)):
        return "Strong password"
    if len(password) >= 8 and any(x.isdigit() for x in password):
        return "Moderate password"
    return "Poor password"

if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    # What does this do?
