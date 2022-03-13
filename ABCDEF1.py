class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()
class B():
    def __init__(self):
        self.b='b'
        print(self.b)
        super().__init__()
class C():
    def __init__(self):
        self.c='c'
        print(self.c)
class D(C):
    def __init__(self):
        self.d='d'
        print(self.d)
        super().__init__()
class E(A):
    def __init__(self):
        self.e='e'
        print(self.e)
        super().__init__()
class F(E,B,D):
    def __init__(self):
        self.f='f'
        print(self.f)
        super().__init__()
f=F()              
        
