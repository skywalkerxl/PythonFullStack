def outer(para):
    x = para
    def inner():
        print(x)

    return inner

outer(4)()  # 调用inner