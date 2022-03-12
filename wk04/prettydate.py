"""
Write a program that converts 24 hour time into 12 hour time.
- You may assume that all inputs will be a valid 24 hour time.
- You program should read each line of input from standard input until EOF and output the result to standard output.

Sample input:
1234
0525
0000
0001
1904

Sample output:
12:34 PM
05:25 AM
00:00 AM
00:01 AM
07:04 PM
"""

import sys
from datetime import datetime

for line in sys.stdin:
    hour = int(line[:2])
    minute = int(line[2:4])
    
    pm = hour >= 12
    if pm and hour != 12:
        hour -= 12
        
    pad_hour = hour < 10
    pad_minute = minute < 10

    result = ''
    if pad_hour:
        result += '0'
    result += str(hour)
    
    result += ':'
    
    if pad_minute:
        result += '0'
    result += str(minute)
    
    if pm:
        result += ' PM'
    else:
        result += ' AM'
        
    print(result)

# Alternative solution 
# for line in sys.stdin:
#     hours = int(line[:2])
#     minutes = int(line[2:4])

#     time_period = "AM"
#     if hours >= 12:
#         time_period = "PM"
#         if hours > 12:
#             hours -= 12

#     print(f"{hours:02}:{minutes:02} {time_period}")

# Another alternative solution
# for line in sys.stdin:
#     time = datetime.strptime(line[:-1], '%H%M')
#     print(time.strftime(f"{'00' if time.hour == 0 else '%I'}:%M %p"))
