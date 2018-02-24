class F:
    def __init__(self):
        pass

    def f1(self):
        print("f1")

    def f2(self):
        print("f2")

class S(F):
    def __init__(self):
        pass

    def s1(self):
        print("s1")

    def f2(self):
        super(S, self).f2()  # 调用父类的方法(推荐)
        F.f2(self)  # 调用父类的方法
        print("s2")


obj = S()

obj.f2()