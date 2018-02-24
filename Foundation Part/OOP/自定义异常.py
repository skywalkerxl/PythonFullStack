class CustomError(Exception):
    def __init__(self, msg):
        self.message = msg

    # 拿到错误信息
    def __str__(self):
        return (self.message)


try:
    raise CustomError("This is my error")
except CustomError as e:
    print(e)