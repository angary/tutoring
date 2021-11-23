# char weather[50];
# scanf("%s", &weather);
weather = input()

# Note in python, we use indentation and colons instead of curly brackets
# We also write "elif" instead of "else if"
if weather == "raining":
    print("You should wear a raincoat when you go out")
elif weather == "sunny":
    print("You should wear a hat when you go out")
else:
    print("Have a nice day")
