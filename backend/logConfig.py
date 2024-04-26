import logging

def configure_logger():
    # Create a logger object with the module name
    logger = logging.getLogger(__name__)

    # Set the logging level (optional, default is WARNING)
    logger.setLevel(logging.WARNING)

    # Create a file handler to log messages to a file
    #file_handler = logging.FileHandler('my_log.log')

    # Create a stream handler to log messages to the console
    stream_handler = logging.StreamHandler()

    # Create a formatter to specify the format of log messages
    formatter = logging.Formatter('%(levelname)s %(message)s')

    # Set the formatter for the handlers
    #file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger if not already added
    if not logger.handlers:
        #logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
