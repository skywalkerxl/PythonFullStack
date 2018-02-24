import time

def logger(flag=""):
    def show_time(func):
        def inner(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("spend time %s" %(end - start))
            if flag == "true":
                print("日志记录")
        return inner

    return show_time

@logger()  # show_time
def add(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    time.sleep(1)

add(1, 2, 3, 4)