#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/18 12:27   ZDD      1.0         None
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        方法1：
            1. 二重循环，在第二重循环进行次数的统计
                错误用例：pwwkew
                错误原因：第二次循环也是从头开始遍历，失去了求解的意义
                错误用例：' '
                错误原因：只有一个字符结果为1

            2. 理清逻辑
                分情况：
                    1. 完全不重复
                    2. 完全重复
                    3. 其他情况
                问题解决：
                    1. 优点：内存占用小
                    2. 缺点：时间复杂度过高
                优化：
                    1. 如何进行空间换时间

        方法2：
            1. 滑动窗口方法
            2. 理清逻辑
                分情况： 滑动窗口则考虑
                    1. 空字符
                    2. 其他情况
        :param s:
        :return:
        """
        res = 0
        str_len = len(s)
        if str_len == 1:
            res = 1
            return res

        for i in range(str_len):
            # 记录当下已经遍历过的字符
            temp_res = 0
            temp_list = []
            for j in range(i, str_len):
                if s[j] in temp_list:
                    break
                else:
                    temp_res += 1
                    temp_list.append(s[j])
            res = temp_res if temp_res > res else res
        return res

    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0
        # 利用集合的无重复性质
        window = set()
        # 定义窗口的左右边界
        l = 0
        window_len = 0
        # 定义最大长度
        res = 0
        # 获取长度
        n = len(s)
        for i in range(n):
            window_len += 1

            while s[i] in window:
                window.remove(s[l])
                l += 1
                window_len -= 1
            if res < window_len:
                res = window_len
            window.add(s[i])
        return res


if __name__ == '__main__':
    so = Solution()
    res = so.lengthOfLongestSubstring("aujgaga")
    print(res)
