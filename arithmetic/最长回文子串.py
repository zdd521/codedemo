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
        1. 中心扩散算法
            1. 分析：如果s[i: j+1]为回文串，那么如果s[i-1] == s[j+1]的话，s[i-1: j+2]也是回文串，因此可以通过中心扩散求解
                1. 中心扩散函数构建：考虑到奇偶特性，若是为奇数子串，则从中心一位开始扩散，若是偶数子串，则从中心两位开始扩散，
                    1. 扩散的方式，采用双指针，此时双指针也可以方便支持判断奇数偶数的扩散
        :param s:
        :return:
        """

        # 定义中心扩散函数
        def center_diffusion(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]


        # 定义初始结果串
        res = ''
        # 遍历整个串
        for i in range(len(s)):
            odd_sub = center_diffusion(s, i, i)
            even_sub = center_diffusion(s, i, i+1)
            res = odd_sub if len(odd_sub) > len(res) else res
            res = even_sub if len(even_sub) > len(res) else res


        return res


if __name__ == '__main__':
    so = Solution()
    res = so.longestPalindrome('cbbd')
    print(res)
