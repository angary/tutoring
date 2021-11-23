"""
Write a program prettydate.py that converts 24 hour time into 12 hour time.

You may assume that all inputs will be a valid 24 hour time.
You program should read each line of input from standard input until EOF and output the result to standard output.

>>> 1234 -> 12:34 PM
>>> 0525 -> 05:25 AM
>>> 0000 -> 00:00 AM
>>> 0001 -> 00:01 AM
>>> 1904 -> 07:04 PM
"""

# Loop through the input
while True:
    line = input()
    
    # Get the hours and minutes
    hours = int(line[:2])
    minutes = int(line[2:])

    # Determine if AM or PM
    am = True
    if hours >= 12:
        am = False
    if hours > 12:
        hours -= 12

    # Print formatted string
    print(f"{hours:02}:{minutes:02} {'AM' if am else 'PM'}")
