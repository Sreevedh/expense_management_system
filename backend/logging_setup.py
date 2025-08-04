import logging

def setup(name, log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    file = logging.FileHandler(log_file)
    formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    file.setFormatter(formater)
    logger.addHandler(file)

    return logger