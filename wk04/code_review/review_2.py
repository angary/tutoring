def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    horrible_pw = ["password", "iloveyou", "123456"]
    digit = False
    upper = False

    if password in horrible_pw:
        return "Horrible Password"
    elif len(password) >= 8:
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                upper = True
        if digit and upper and len(password) >= 12:
            return "Strong Password"
        elif digit:
            return "Moderate Password"
    
    return "Poor Password"

if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    # What does this do?
