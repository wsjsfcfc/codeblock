# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
from test import test

logger = logging.getLogger()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')
    logger.setLevel(logging.ERROR)
    try:
        test()
    except Exception as exception:
        logger.debug("test")
        logger.exception(exception)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
