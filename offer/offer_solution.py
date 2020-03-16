#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao


"""
题目: 在一个二维数组中,每一行都按照从左到右递增的顺序排列,每一列都按照从上到下递增的顺序排序。请完成一个函数,
输入这样的一个二维数组和一个整数,判断数组中是否含有该整数。
"""

from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    """
    题目: 在一个二维数组中,每一行都按照从左到右递增的顺序排列,每一列都按照从上到下递增的顺序排序。请完成一个函数,
    输入这样的一个二维数组和一个整数,判断数组中是否含有该整数。
    """
    def find_in_two_dimensional_array(self, arrays: List[List[int]], target: int) -> bool:
        row = len(arrays)
        if row < 1:
            return False
        col = len(arrays[0])
        if col < 1:
            return False
        for line in arrays:
            if target in line:
                return True
        return False

    def binary_search_in_two_dimensional_array(self, arrays: List[List[int]], target: int) -> bool:
        row = len(arrays) -1
        if row < 1:
            return False
        col = len(arrays[0]) -1
        if col < 1:
            return False
        i = 0
        j = col
        while i <= row and j >= 0:
            if target < arrays[i][j]:
                j = j - 1
            elif target > arrays[i][j]:
                i = i + 1
            else:
                return True
        return False


    """
    题目:请实现一个函数，将一个字符串中的每个空格替换成“%20”。
    例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
    """
    def replace_blank(self, string: str) -> str:
        temp = ""
        for char in string:
            if char == " ":
                temp = temp + "%20"
            else:
                temp = temp + char
        return temp


    """
    题目:输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
    """
    def reverse_linklist_and_print(self, head: List) -> List[int]:
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        arrayList = []
        while prev:
            arrayList.append(prev.val)
            prev = prev.next

        return arrayList

    """输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。"""

