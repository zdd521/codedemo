#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/13 3:16   lbs      1.0         None
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        1. 构建空矩阵 矩阵的列数矩阵的行数
            1. 行数已知
            2. 列数为周期乘以每个周期的列数
                1. 计算每个周期的列数
                    1. 大于3
                    2. 小于3
        2. 开始填补
            1. 下填补
            2. 右上填补
        :param s:
        :param numRows:
        :return:
        """
        s_len = len(s)
        if numRows ==1 or numRows >= s_len:
            return s
        # cycle_cols
        c_col = 1 + (numRows - 2 if numRows > 2 else 0)
        # cycle_nums
        c_ele_nums = numRows + c_col - 1
        # cols
        cys = s_len / c_ele_nums
        if cys % 1:
            cys += 1
        cys = int(cys)
        cols = cys * c_col
        # make matrix
        res_matrix = [['' for _ in range(cols)] for _ in range(numRows)]
        # make point
        x, y = 0, 0
        # 填补矩阵
        for i, ch in enumerate(s):
            res_matrix[x][y] = ch
            if i % c_ele_nums < numRows - 1:
                x += 1
            else:
                y += 1
                x -= 1
        return ''.join(ch for row in res_matrix for ch in row)




if __name__ == '__main__':
    a = Solution()
    res = a.convert('ABCD', 2)
    print(res)
