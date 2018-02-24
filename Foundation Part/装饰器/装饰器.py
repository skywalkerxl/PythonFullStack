import time

def show_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("spend time: %s" %(end - start))

    return inner

# the tangguo of python provide
@show_time  # foo = show_time(foo)
def foo():
    print("foo...")
    time.sleep(1)

def bar():
    print("bar...")
    time.sleep(1)

@show_time
def add(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    print("result is %s" %(sum))
    time.sleep(1)

add(1, 2, 3, 4, 5)