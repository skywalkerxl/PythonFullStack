# Python中一切事物都是对象

class MyType(type):
    def __init__(self, *args, **kwargs):
        print("123")

    def __call__(self, *args, **kwargs):
        print("MyType call")

class Foo(object, metaclass=MyType):
    def __init__(self):
        print("Foo init")

    def func(self):
        print("hello world")

    def __new__(cls, *args, **kwargs):
        return "对象"

obj = Foo()

# obj是对象, Foo类
# Foo类也是一个对象， type的对象