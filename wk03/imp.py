"""
This is fine, and is useful when using many functions from an import
"""
import foo
print(foo.bar('hi'))


"""
This is like (#1), except useful when the name of the import is quite generic
and could be confused with something else

More commonly, you may see examples like: "import matplotlib.pylot as plt" or
"import numpy as np" which is used to rename modules to something shorter
"""
import foo as fooFile
print(fooFile.bar('hi'))


"""
This is often useful when you only need to import very particular functions from
a file
"""
from foo import bar
print(bar('hi'))


"""
This is not recommended, this imports a whole number of functions that could
conflict with other names in the namespace
"""
from foo import *
print(bar('hi'))


"""
Why does the following not work?

The following code did not work as there was no "global name" in the foo file
As a result, the function was declaring it's own variable called name
"""
import foo

print(foo.getName())
foo.editName('Hayden')
print(foo.getName())
