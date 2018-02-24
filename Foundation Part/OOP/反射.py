#  反射可以跨模块使用

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "%s-%s" %(self.name, self.age)

obj = Foo('Lang', 18)

# getattr　用于返回一个对象的属性值
func = getattr(obj, 'show')
print(func)
r = func()
print(r)

# setattr  给一个对象设置属性值，保存在对象的内存里
setattr(obj, 'k1', 'v1')
print(obj.k1)

# hasattr  判断一个对象是否含有属性值
print(hasattr(obj, 'k1'))

# delattr