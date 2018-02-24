class Bar:
    def __init__(self, name, age, gender):
        self.name = name;
        self.age = age
        self.gender = gender
        print("构造方法")

    def foo(self):
        print(self.name, self.age, self.gender)


bar = Bar("Lang", "100", "male")
bar.foo()