from ayrmath.vec3 import Vec3

class Trixel:
    pos = None

    def __init__(self, pos = Vec3(0,0,0)):
        self.pos = pos

    

    def __repr__(self):
        return '{pos: '+str(self.pos)+'}'