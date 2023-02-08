#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/20 12:32   zdd715      1.0         None
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        分析情况：
            1. 长度为1自动返回
        :param s:
        :return:
        """
        # 获取长度
        size = len(s)
        # 处理特殊
        if size == 1:
            return s
        # 定义temp长度与返回长度
        temp_len = 1
        re_len = 1
        # 定义初始下标
        start = 0
        # 状态表
        dp = [[False for _ in range(size)] for _ in range(size)]
        # 填充状态表
        for j in range(1, size):
            for i in range(j):
                if j - i <= 2:
                    if s[j] == s[i]:
                        dp[i][j] = True
                        temp_len = j - i + 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        temp_len = j - i + 1
                if dp[i][j]:
                    (re_len, start) = (temp_len, i) if re_len < temp_len else (re_len, start)
        return s[start: start + re_len]


if __name__ == '__main__':
    so = Solution()
    res = so.longestPalindrome('ccc')
    print(res)
