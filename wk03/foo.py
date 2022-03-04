def bar(txt):
    return txt


name = 'Ralph'


def editName(string):
    # The `global name` needs to be added so that python knows that it is
    # modifying the global name variable instead of creating a new local
    # variable
    global name
    name = string


def getName():
    return name
