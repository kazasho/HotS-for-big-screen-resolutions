import logging

class LoggerFactory(object):

    _LOG = None

    @staticmethod
    def __create_logger(log_file, log_level):
        """
        A private method that interacts with the Python logging module
        """
        # Set the logging format
        
        log_format = "%(asctime)s:%(levelname)s:%(message)s"

        # Initiate the class variable with logger object

        LoggerFactory._LOG = logging.getLogger(log_file)
        logging.basicConfig(level=logging.INFO, format=log_format, datefmt="%Y-%m-%d %H:%M:%S")

        # Set logging level based on user selection

        if log_level == "INFO":
            LoggerFactory._LOG.setLevel(logging.INFO)
        elif log_level == "ERROR":
            LoggerFactory._LOG.setLevel(logging.ERROR)
        elif log_level == "DEBUG":
            LoggerFactory._LOG.setLevel(logging.DEBUG)
        return LoggerFactory._LOG
    
    @staticmethod
    def get_logger(log_file, log_level):
        """
        A static method called by other modules to initialize logger in their own module
        """
        logger = LoggerFactory.__create_logger(log_file, log_level)

        # Return the logger object
        return logger