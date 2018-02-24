# 公有成员
# 私有成员


class Foo:
    def __init__(self, name, age):
        self.name = name
        #　私有成员，外部无法［直接］访问
        self.__age = age

class F:
    def __init__(self):
        self.ge = "ge"
        self.__gene = "__gene"

class S(F):
    def __init__(self, name):
        self.name = name
        self.__age = 18
        super(S, self).__init__()

    def show(self):
        print(self.ge)
        print(self.name)
        print(self.__age)
        # print(self.__gene)

obj = S("lang")
obj.show()