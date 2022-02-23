def set_name(first_name, middle_name, last_name):
    """
    Set name implementation which returns if a name can be set according to the
    rules (currently only checks first and last name length)
    """
    if not len(first_name) >= 3 or not len(first_name) <= 30:
        return False
    
    if not len(last_name) >= 3 or not len(last_name) <= 50:
        return False
    
    return True


# Write example test
# Good tests are those that test the edge cases

# This is a way to make a string have exactly 51 characters
print(set_name("iii", "love", "0"*51))
