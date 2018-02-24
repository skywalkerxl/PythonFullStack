class Foo:

    # 普通方法也保存在类中，由对象来调用  self => 对象
    def bar(self):
        print('bar')

    @staticmethod  # 静态方法装饰器
    def sta():
        print("123")

    @classmethod
    def classmtd(cls):
        # cls是类名，不依赖对象， cls => 当前类
        print(cls)
        print('classmd')

    # 应用场景
    #   如果对象中需要保存一些值，执行某功能时需要使用对象中的值 -> 普通方法
    #   不需要任何对象中的值，用静态方法，

obj = Foo()  # 不管是类执行还是对象执行，必须得先创建一个对象

Foo.bar(obj)
Foo.sta()
Foo.classmtd()