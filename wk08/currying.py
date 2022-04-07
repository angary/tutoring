def f():
    def g():
        return 1
    return g

def i(x):
    def j(y):
        return x + y
    return j

print(f)
print(f())
print(f()())
print(i(1))
print(i(1)(2))
