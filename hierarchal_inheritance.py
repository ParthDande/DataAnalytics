#code for hierarchal inheritance

# Class A is the parent class
class A :
    a = 10
    def __init__(self):#constuctor of class A
        print("Constructor of CLASS A")

    def fun1(self):
        print("class A function")
class B(A):
    #this is the child class
    b = 20
    def __init__(self):
        print("Constructor of CLASS B")

    def fun2(self):
        print("Class B function")
class D(B):
    def __init__(self):
        print("constructor of class D")
    
    def functiond(self):
        print("Function of class D")

class C(A):
    c = 30
    #this is the sub child of class B
    def __init__(self):
        print("Constructor of class C")

    def fun3(self):
        print("This is the function of class C")  

class E(C):
    def __init__(self):
        print("This is the constructor of class E")
    def functionE(self):
        print("this is the function of class E")
obj = A()#objct of class 1
obj.fun1()
obj1 = B()#object of class2 
obj1.fun1()#calling the method of class A using object of class B
#printed variable of class A using object of CLass B
#print(obj1.a)
obj4 = D()
print(obj4.b)
