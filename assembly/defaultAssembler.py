import logging
from ayrmath.trixel import Trixel
from ayrmath.vec3 import Vec3


def assembleWorld(paramry):
    world = {}
    world['name'] = paramry['baseparams']['name']
    world['foundation'] = []

    testpoint = Trixel(Vec3(1,2,3))
    logging.debug(str(testpoint))

    return world