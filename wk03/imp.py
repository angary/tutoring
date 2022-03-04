print(foo.bar('hi')) # 1

# You would use this when you want to rename the module because
# - The module has the same name as another variable
# - Moreoften, sometimes people do this to give variables a more
#   meaningful name, or a shorter name
import foo as fooFile
print(fooFile.bar('hi')) # 2

# This is good if you don't need all the functions, and it
# makes it a bit shorter to call the functions
from foo import bar
print(bar('hi')) # 3

# This can be problematic, because when we import ALL the functions
# there can be namespace conflicts
from foo import *
print(bar('hi')) # 4


"""
Why does the following function not behave as intended?
- Because there was no global keyword used in editName
"""
import foo

print(foo.getName())
foo.editName('Hayden')
print(foo.getName())
