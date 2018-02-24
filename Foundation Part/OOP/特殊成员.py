# 特殊成员
# __init__  类()自动执行
# __call__  对象()  类()()  自动执行
# __int__   int(对象)
# __str__   str()

class Foo:
    def __init__(self):
        print("init")

    def __call__(self):
        print("call")

    def __int__(self):
        return 1

    def __str__(self):
        return "string"

    # 执行加法操作
    def __add__(self, other):
        """

        :param other: + 后面的
        :return:
        """
        return 123

    # 对象被销毁时，自动执行,不怎么用
    def __del__(self):
        pass

    def __dict__(self):
        """
        将对象中封装的所有内容以字典的形式返回
        :return:
        """

    def __setitem__(self, key, value):
        print("赋值")

    def __getitem__(self, item):
        print("取值")
        print(item, type(item))

    def __delitem__(self, key):
        print("删除，del 对象 操作")

obj = Foo()
obj()
ret = int(obj)
print(ret)
_str = str(obj)
print(_str)
print(Foo.__dict__)