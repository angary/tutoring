import foo
print(foo.bar('hi')) # 1

import foo as fooFile
print(fooFile.bar('hi')) # 2

from foo import bar
print(bar('hi')) # 3

from foo import *
print(bar('hi')) # 4


"""
Why does the following function not behave as intended?
"""
# import foo

# print(foo.getName())
# foo.editName('Hayden')
# print(foo.getName())
