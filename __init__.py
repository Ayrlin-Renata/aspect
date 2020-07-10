def _import_all_modules(folder):
    """ Dynamically imports all modules in this package. """
    import traceback
    import os
    global __all__
    __all__ = []
    globals_, locals_ = globals(), locals()
    
    # Dynamically import all the package modules in this file's directory.
    for filename in os.listdir(folder):
        # Process all python files in directory that don't start
        # with underscore (which also prevents this module from
        # importing itself).
        if filename[0] != '_' and filename.split('.')[-1] in ('py', 'pyw'):
            modulename = filename.split('.')[0]  # Filename sans extension.
            package_module = '.'.join([folder, modulename])
            try:
                module = __import__(package_module, globals_, locals_, [modulename])
            except:
                traceback.print_exc()
                raise
            for name in module.__dict__:
                if not name.startswith('_'):
                    globals_[name] = module.__dict__[name]
                    __all__.append(name)

_import_all_modules('ingest')