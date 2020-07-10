import logging
import assemblycontrol

def main(paramry):
    logging.info('RECIEVING ASPECT COMMAND')
    
    logging.info('BEGIN WORLD ASSEMBLY')
    world = assemblycontrol.assembleWorld(paramry)
    
    return