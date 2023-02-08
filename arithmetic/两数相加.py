#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/7 19:03   lbs      1.0         None
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. 相加
            1. 进位
                1. 前n-1个进位
                2. 第n个进位
        2. 递归
            1. 每一步的操作无非是相加，在此基础上进行递归
                1. 考虑进位
        3.
        :param l1:
        :param l2:
        :return:
        """
        # 解法1
        # 初始化需要的数据
        # res_list = ListNode(val=0)
        # temp_node = res_list
        # temp_l1, temp_l2 = l1, l2
        # flag = -1
        #
        # # 等位相加
        # while temp_l1 and temp_l2:
        #
        #     temp_node.val = temp_l1.val + temp_l2.val + (0 if flag == -1 else 1)
        #     flag = temp_node.val - 10 if temp_node.val > 9 else -1
        #     if flag != -1:
        #         temp_node.val = flag
        #
        #     temp_l1, temp_l2 = temp_l1.next, temp_l2.next
        #
        #     if temp_l1 or temp_l2:
        #         # 这里是错的
        #         temp_node.next = ListNode(val=-1)
        #         temp_node = temp_node.next
        #
        # if temp_l1:
        #     while temp_l1:
        #         temp_node.val = temp_l1.val + (0 if flag == -1 else 1)
        #         flag = temp_node.val - 10 if temp_node.val > 9 else -1
        #         temp_l1 = temp_l1.next
        #         if flag != -1:
        #             temp_node.val = flag
        #         if temp_l1:
        #             temp_node.next = ListNode(val=-1)
        #             temp_node = temp_node.next
        #
        # elif temp_l2:
        #     while temp_l2:
        #         temp_node.val = temp_l2.val + (0 if flag == -1 else 1)
        #         flag = temp_node.val - 10 if temp_node.val > 9 else -1
        #         temp_l2 = temp_l2.next
        #         if flag != -1:
        #             temp_node.val = flag
        #         if temp_l2:
        #             temp_node.next = ListNode(val=-1)
        #             temp_node = temp_node.next
        # if flag != -1:
        #     temp_node.next = ListNode(val=1)
        # return res_list
        # 解法2
        # # 考虑递归出口
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        #
        # l1.val = l1.val + l2.val
        #
        # # 考虑val>9
        # if l1.val > 9:
        #     # 构建了进位的next节点
        #     l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
        #     l1.val = l1.val % 10
        #
        # l1.next = self.addTwoNumbers(l1.next, l2.next)
        #
        # return l1
        # 解法3
        head = ListNode()
        temp_node = head
        temp = 0
        while temp or l1 or l2:
            val = temp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next

            temp = val // 10
            val = val % 10

            # 构建链表
            temp_node.next = ListNode(val=val)
            temp_node = temp_node.next

        return head.next


if __name__ == '__main__':
    # 实例化
    Solu = Solution()
