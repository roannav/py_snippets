import logging

CURRENT_LEVEL = logging.DEBUG   # show ALL log messages
#CURRENT_LEVEL = logging.INFO    # show INFO, WARNING, ERROR and CRITICAL logs
#CURRENT_LEVEL = logging.WARNING # show WARNING, ERROR and CRITICAL logs
#CURRENT_LEVEL = logging.ERROR   # show only ERROR and CRITICAL log messages
#CURRENT_LEVEL = logging.CRITICAL # show only CRITICAL log messages

# To log to the screen, don't include a filename arg
logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# To log to a file, include the filename arg
#logging.basicConfig( filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('BEGIN')

i=4
logging.debug(f'i is {i}')

logging.info('User registration complete.')
logging.warning('You have called a soon to be deprecated function.')
logging.error('Failed to save data.')
logging.critical('Crash is imminent!')

# Stops all log messages that are CRITICAL level and below.
# ie Stops ALL log messages
logging.disable(logging.CRITICAL) 

logging.info('This will not be logged.')
logging.error('Not logged either.')
