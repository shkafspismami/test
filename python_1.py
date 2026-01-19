import time


def hello_func(name):
    for _ in range(1, 6):
        print(f"{_}...")
        time.sleep(1)

    print(f"Hello Everyone! and {name}!")

def bye_func(name):

    print (f"Bye Everyone! and {name}")


def test_func(*args):
    print(args)


hello_func("Kenny")
bye_func("Kenny")
test_func(1, 2, 3)