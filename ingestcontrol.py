import os.path, pkgutil, logging, importlib

# MAIN INGEST FUNCTION
def ingestParams():
    paramry = {}

    # locate all modules
    pkgpath = os.path.dirname(__file__)+"\\ingest"
    logging.debug('Scanning for ingest modules in: '+pkgpath)
    modules = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
    logging.debug('Found: '+str(modules))

    # ingest modules
    for mod in modules:
        modname = 'ingest.'+mod
        logging.debug('Ingesting '+modname)
        imod = importlib.import_module(modname)
        # get param data
        paramry[mod] = (imod.getParams())

    return paramry