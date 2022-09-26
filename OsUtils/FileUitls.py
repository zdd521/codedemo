import os
from shutil import rmtree


class FileOperation:

    @classmethod
    def create_empty_file(cls, file_name: str = None):
        """

        :param file_name:
        :return:
        """
        try:
            if os.path.exists(file_name):
                print(f'{file_name} is already exists!')
                for name in os.listdir(file_name):
                    name = os.path.join(os.path.abspath(file_name), name)
                    print(f'deleting {name}······')
                    rmtree(name)
                    print('file created done!')
            else:
                print(f'creating {file_name}')
                os.mkdir(file_name)
        except Exception as e:
            raise ValueError(f'{e}')


if __name__ == '__main__':
    demo = FileOperation()
    demo.create_empty_file('./test')
