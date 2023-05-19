class A():
    def __init__(self):
        print("Constructor A")
    def functionA(self):
        print("function of A")


class B(A):
    def __init__(self):
        print("Constructor B")
    def functionB(self):
        print("function of B")

class C(A):
    def __init__(self):
        print("Constructor C")
    def functionC(self):
        print("function of C")

obj = A()
obj1 = B()
obj2 = C()
obj.functionA()
obj2.functionA()
