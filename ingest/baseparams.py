import logging

def getParams():
    params = {}
    logging.debug('Baseparams ingest module reporting for duty.')

    logging.info('Enter resolution:')
    _input = input()
    if not _input:
        _input = 8 #default
    params['resolution'] = int(_input)

    logging.info('Enter world assembly module:')
    _input = input()
    if not _input:
        _input = "defaultAssembler" #default
    params['assemblymodule'] = str(_input)

    return params