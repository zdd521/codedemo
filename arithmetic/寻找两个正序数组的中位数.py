#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/19 17:22   zdd715      1.0         None
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """

        :param nums1:
        :param nums2:
        :return:
        """
        def get_num(k):
            index1, index2 = 0, 0
            while True:
                # 完成出口
                if index1 == len_1:
                    return nums2[index2 + k - 1]
                if index2 == len_2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                new_index1 = min(index1 + k//2 - 1, len_1 -1)
                new_index2 = min(index2 + k//2 - 1, len_2 -1)
                temp_data_1, temp_data_2 = nums1[new_index1], nums2[new_index2]
                if temp_data_1 <= temp_data_2:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1
                    pass
                else:
                    k -= new_index2 -index2 +1
                    index2 = new_index2 + 1

                pass
            pass

        # 分情况
        len_1, len_2 = len(nums1), len(nums2)
        total_len = len_1 + len_2
        if total_len % 2 == 1:  # 奇数
            re_data = get_num(total_len // 2 + 1)
        else:   # 偶数
            re_data = (get_num(total_len // 2) + get_num(total_len // 2 + 1)) / 2
        return re_data


if __name__ == '__main__':
    # 1 2 3 4 5 6
    a = list(range(1, 4))
    b = list(range(4, 7))
    solu = Solution()
    res = solu.findMedianSortedArrays(a, b)
    print(res)