class Foo:

    # 静态字段, 保存在类中，执行 可以通过对象访问，也可以通过类访问
    county = "中国"

    def __init__(self, name):
        # 普通字段，保存在对象中，执行只能通过对象访问
        self.name = name

    # 普通方法
    def bar(self):
        print("bar")

    @property
    def per(self):
        print("123")

    @per.setter
    def per(self, val):
        print(val)

    @per.deleter
    def per(self):
        print("delete")

    def f2(self, v):
        print(v)

    def f3(self):
        print("delete")
    per1 = property(fget=bar, fset=f2, fdel=f3, doc="这是介绍内容")  # 这和property的作用差不多

foo = Foo("安徽")
print(foo.county)
print(foo.name)
foo.per
foo.per = 12
del foo.per
foo.per1 = "set123"