import os
import logging


class Log:

    def __init__(self, ):
        self.log_2_file()

    @classmethod
    def log_2_file(cls, flag: bool = True, file_name: str = None, log_type=logging.INFO):
        """

        :param log_type:
        :param flag:
        :param file_name:
        :return:
        """
        file_name = os.path.join(os.path.dirname(__file__), 'log.txt') if not file_name else file_name
        if not os.path.exists(file_name):
            file_create = open(file_name, 'w', encoding='utf-8')
            file_create.close()
        if flag:
            logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                                       '- %(levelname)s: %(message)s', filename=file_name, level=log_type)
        else:
            logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                                       '- %(levelname)s: %(message)s', level=log_type)

    @classmethod
    def loginfo(cls, text: str = None):
        """

        :param text:
        :return:
        """
        logging.info(msg=text)
