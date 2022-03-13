class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
        super().__init__()
class C(object):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
class D(object):
    def __init__(self):
        self.d='d'
        print(self.d)
        super().__init__()
class E(object):
    def __init__(self):
        self.e='e'
        print(self.e)
class F(A,B,C,D,E):
    def __init__(self):
        self.f='f'
        print(self.f)
        super().__init__()
f=F()              
        
