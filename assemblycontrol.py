import os.path, pkgutil, logging, importlib

def assembleWorld(paramry):
    world = None

    """
    # locate all modules
    pkgpath = os.path.dirname(__file__)+"\\assembly"
    logging.debug('Scanning for assembly modules in: '+pkgpath)
    modules = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
    logging.debug('Found: '+str(modules))
    """

    modname = 'assembly.'+paramry['baseparams']['assemblymodule']
    logging.info('DELEGATING WORLD ASSEMBLY TO ' + modname)
    imod = importlib.import_module(modname)
    # offload world assembling
    world = imod.assembleWorld(paramry)

    return world