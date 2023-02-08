#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/19 13:29   lbs      1.0         None
"""


class ListTools:

    @classmethod
    def join_two_sorted_list(cls, list1: list, list2: list):
        """

        :param list1:
        :param list2:
        :return:
        """
        # 获取两者长度
        len1, len2 = len(list1), len(list2)
        # 定义返回的数组
        res = []
        # 定义索引
        i, j = 0, 0
        while i < len1 and j < len2:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        res += list1[i:len1]
        res += list2[j:len2]

        return res


if __name__ == '__main__':
    a = [1, 2, 5, 6]
    b = [3, 4]
    print(ListTools.join_two_sorted_list(list1=a, list2=b))
