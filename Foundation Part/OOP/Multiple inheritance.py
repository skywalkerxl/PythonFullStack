class F0:
    def a(self):
        print("F0.a")

class F1(F0):
    def a1(self):
        print("F1.a")

class F2:
    def a(self):
        print("F2.a")

class S(F1, F2):
    def __init__(self):
        pass

obj = S()
obj.a()  # F0.a

class BaseRequestHandler():
    pass

class RequestHandler(BaseRequestHandler):
    def server_forever(self):
        print("server_forever")
        self.process_request()

    def process_request(self):
        print('minx.process_request')

class Minx:
    def process_request(self):
        print('minx.process_request')

class Son(Minx, RequestHandler):
    pass


obj = Son()
obj.server_forever()