token = "asdf"

def echo_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

def validate(function):
    def wrapper(token, *args):
        if token != "asdf":
            raise ValueError("invalid token")
        return function(token, *args)
    return wrapper

@validate
def say_hi_to(token, name):
    print("hi", name)

@validate
def print_bye(token):
    print("bye")

@validate
def get_password(token):
    return "password"


if __name__ == "__main__":
    # echo_args(1, 2, 3, name="John", age=30)
    say_hi_to("asdf", "gary")
    print_bye("asdf")
    # print(get_password("asdf"))

