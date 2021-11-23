def check_password(password):
    
    if password == "password" or password == "iloveyou" or password == "123456":
        return "Horrible password"
    elif (len(password) >= 12 and any(x.isupper() for x in password) and
        any(x.isdigit() for x in password) and 
        any(x.islower() for x in password)):
        return "Strong password"
    elif len(password) >= 8 and any(x.isdigit() for x in password):
        return "Moderate password"
    else:
        return "Poor password"
   
if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    # What does this do? 
