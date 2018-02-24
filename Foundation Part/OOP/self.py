class Bar:
    def foo(self, arg):
        print(self)  # self 代指，调用方法的对象

bar = Bar()

bar.foo(1)