def cube(x):
    return x ** 3

# int number;
# printf("Please enter a number: ");
# scanf("%d", &number);
number = int(input("Please enter a number: "))
# number = "10"
# number = 10

# int result = cube(number);
result = cube(number)

# printf("The cube of the number you have entered is %d\n.", result);
print(f"The cube of the number you have entered is {result}")
