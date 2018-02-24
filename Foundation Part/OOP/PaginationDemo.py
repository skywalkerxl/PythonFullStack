class Pagination:
    def __init__(self, currentPage):
        try:
            self.page = int(currentPage)
        except Exception as e:
            self.page = 1
            print(e)

    @property
    def start(self):
        p = (self.page - 1) * 10

        return p

    @property
    def end(self):
        p = self.page * 10
        return p

li = []

for i in range(100000):
    li.append(i)

obj = Pagination("1")
print(li[ obj.start : obj.end ])