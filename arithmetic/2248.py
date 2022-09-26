from typing import List


class Solution:
    # def intersection(self, nums: List[List[int]]) -> List[int]:
    #     """
    #
    #     :param nums:
    #     :return:
    #     """
    #     # 第一次遍历找出每个列表中最大的数字max和最小数字min，利用max和min构建查找字典，查找字典需要为一个列表
    #     # 也不一定要为一个列表只要保证为1，每一次遍历存在一个不在的情况则为0
    #     # 定义全局量
    #     min_num = 0
    #     max_num = 0
    #     for ele_list in nums:
    #         max_num = max(max(ele_list), max_num)
    #         min_num = min(min(ele_list), min_num)
    #     # 构建查找字典
    #     find_dict = {i: 1 for i in range(min_num, max_num + 1)}
    #     for ele_list in nums:
    #         for key in find_dict.keys():
    #             if not key in ele_list:
    #                 find_dict[key] = 0
    #     # 对字典按键排序
    #     res = sorted([key for key, value in find_dict.items() if value])
    #     return res
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for ele in nums[1:]:
            tmp = set()
            for num in ele:
                if num in res:
                    # 元组调用add方法
                    tmp.add(num)
            res = tmp
            # 学习对时间复杂度的分析，sorted的排序是timesort，最快为O(n)，平均为O(nlogn)，最糟糕为O(nlogn)
        return sorted(res)


if __name__ == '__main__':
    nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    solu = Solution()
    res = solu.intersection(nums=nums)
    print(res)
