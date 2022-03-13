class Y(object):
    def __init__(self):
        self.y='y'
        print(self.y)
        super().__init__()
class O():
    def __init__(self):
        self.o='o'
        print(self.o)
        super().__init__()        
class H(O):
    def __init__(self):
        self.h='h'
        print(self.h)
        super().__init__()        
class C(H):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
class E():
    def __init__(self):
        self.e='e'
        print(self.e)
        super().__init__()
class M():
    def __init__(self):
        self.p='p'
        print(self.p)
        super().__init__()        
class F(M):
    def __init__(self):
        self.e='e'
        print(self.e)
        super().__init__()        
class D(E):
    def __init__(self):
        self.d='d'
        print(self.d)
        super().__init__()
class S(Y):
    def __init__(self):
        self.s='s'
        print(self.s)
        super().__init__()
class U():
    def __init__(self):
        self.u='u'
        print(self.u)
        super().__init__()        
class P(S,C,D,F,U):
    def __init__(self):
        self.p='p'
        print(self.p)
        super().__init__()
p=P()              
        
