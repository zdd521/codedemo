# 进行各种过滤操作
class ListFilter:

    @classmethod
    def filter_list_num(cls, input_list: list):
        """
        方法1：调用filter与lambda表达式
        方法2：调用列表生成式
        :param input_list:
        :return:
        """
        if input_list:
            # 方法1   这里注意filter返回的filter对象，需要将该对象传递给相应库函数去使用
            re_list = list(filter(lambda x: isinstance(x, int) or isinstance(x, float), input_list))
            # 方法2
            # re_list = [i for i in input_list if isinstance(i, int) or isinstance(i, float)]
        else:
            print('List is Null')
            re_list = []
        return re_list

    @classmethod
    def total_list_num(cls, input_list: list):
        pass


if __name__ == '__main__':
    demo = ListFilter()
    res = demo.filter_list_num([1, 1, 3.5, 6, 'a'])
    print(res)
