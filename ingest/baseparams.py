import logging

def getParams():
    params = {}
    logging.debug('Baseparams ingest module reporting for duty.')

    logging.info('Enter world name:')
    _input = input()
    if not _input:
        _input = "unloved" #default
    params['name'] = str(_input)
    
    logging.info('Enter world assembly module:')
    _input = input()
    if not _input:
        _input = "defaultAssembler" #default
    params['assemblymodule'] = str(_input)
    
    logging.info('Enter resolution:')
    _input = input()
    if not _input:
        _input = 8 #default
    params['resolution'] = int(_input)


    return params