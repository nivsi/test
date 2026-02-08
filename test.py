class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class B:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z       


class C(A, B):
    def __init__(self, x, y, z):
        super.__init__(x,y,z) 
        super.__init__(x,y)            