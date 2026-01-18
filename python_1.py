import time

def timer(seconds):
    for _ in range(1, seconds+1):
        print(f"{_}...")
        time.sleep(1)

def hello_func(name, seconds = 3):
    timer(seconds)
    print(f"Hello Everyone! and {name}!")

def bye_func(name, seconds = 3):
    timer(seconds)
    print (f"Bye Everyone! and {name}")

hello_func("Kenny")
bye_func("Kenny", 2)