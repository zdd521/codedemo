#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/7 0:58   lbs      1.0         None
"""


# [3,2,4] 6
def tow_nums(nums: list, target: int):
    """

    :param nums:
    :param target:
    :return:
    """
    for i in range(1, len(nums)):
        temp_list = nums[:i]
        if target - nums[i] in temp_list:
            return [i, nums.index(target - nums[i])]


if __name__ == '__main__':
    res = tow_nums([3, 2, 4], 6)
    print(res)