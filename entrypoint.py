print('INITIALIZING WORLD ENGINE...')

# IMPORTS
import sys, getopt
import logging

import ingestcontrol
import aspectcontrol

# GLOBAL VARS
loglevel = None


# MAIN
def main(argv):
    # init
    parseOpts(argv)
    initLogger()

    logging.debug('Init finished.')

    # ingest
    logging.debug('Ingesting parameters.')
    logging.info('ACQUIRING WORLD PARAMETERS')
    paramry = ingestcontrol.ingestParams()
    logging.debug('Parameters ingested:')
    logging.debug(str(paramry))

    # transfer control
    logging.info('CEDING APPLICATION PROCESS TO ASPECT CONTROL')
    aspectcontrol.main(paramry)
    
    # done

#
# STARTUP FUNCS
#
def parseOpts(argv):
    global loglevel
    try:
        opts, args = getopt.getopt(argv,"hl:",["loglevel="])
    except getopt.GetoptError:
        print('test.py -l <loglevel>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -l <loglevel>')
            sys.exit()
        elif opt in ("-l", "--loglevel"):
            loglevel = arg
    if not loglevel:
        loglevel = 'DEBUG' #change later 

def initLogger():
    global loglevel
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)
    logging.debug('Logger ready.')

if __name__ == "__main__":
    main(sys.argv[1:])