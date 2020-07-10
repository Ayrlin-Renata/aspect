class Vec3:
    r = 0 # radius
    t = 0 # theta (vert / xy-axis / latitude)
    p = 0 # phi (horizontal / z-axis / longditude)

    def __init__(self, r=0, t=0, p=0):
        self.r = r
        self.t = t
        self.p = p

    def setpos(self, lr, lt, lp):
        self.r = lr
        self.t = lt
        self.p = lp

    def zeropos(self): 
        self.r = 0
        self.t = 0
        self.p = 0

    def __add__(self, vec3):
        self.r += vec3.r
        self.t += vec3.t
        self.p += vec3.p
        return self

    def __sub__(self, vec3):
        self.r -= vec3.r
        self.t -= vec3.t
        self.p -= vec3.p
        return self

    def __eq__(self, vec3):
        return self.r == vec3.r and self.t == vec3.t and self.p == vec3.p

    def __repr__(self):
        return '<'+str(self.r)+', '+str(self.t)+', '+str(self.p)+'>'