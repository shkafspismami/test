import time

def hello_func(name):
    for _ in range(1, 6):
        print(f"{_}...")
        time.sleep(1)

    print(f"Hello Everyone! and {name}!")

hello_func("Kenny")