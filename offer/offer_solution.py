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

    def __init__(self):
        self.fib_map = {}
        self.fib_dict = {}
        self.frog_ans = {0:0, 1:1, 2:2}
        self.frog_ans_n = {0:0, 1:1, 2:2}
        self.rectangle_map = {1:1, 2:2}

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
    def reConstructBinaryTree(self, pre: List[int], tin: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        n = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:n+1], tin[:n])
        root.right = self.reConstructBinaryTree(pre[n+1:], tin[n+1:])
        return root

    """
    题目:把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
         输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
         例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    """
    def rotate_part_of_array(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 1:
            return 0
        min_num = nums[0]
        for i in range(size):
            min_num = min(min_num, nums[i])
        return min_num

    """
    题目:构造斐波那契数列,要求输入一个整数n,输出斐波那契数列的第n项
    """
    def fib_up_down(self, n: int) -> int:
        if n in self.fib_map:
            return self.fib_map[n]
        else:
            if n <= 1:
                f = n
            else:
                f = self.fib_up_down(n-1) + self.fib_up_down(n-2)
            self.fib_map[n] = f
        return f

    def fib_bottom_up(self, n: int) -> int:
        for i in range(n+1):
            if i <= 1:
                f = i
            else:
                f = self.fib_dict[i-1] + self.fib_dict[i-2]
            self.fib_dict[i] = f
        return self.fib_dict[n]

    """
    题目:一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法?
    """
    def count_frog_jump_way(self, n: int) -> int:
        if n in self.frog_ans:
            return self.frog_ans[n]
        else:
            ans = self.count_frog_jump_way(n-1) + self.count_frog_jump_way(n-2)
            self.frog_ans[n] = ans
        return ans

    """
    题目:一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
    """
    def count_frog_jump_way_n(self, n: int) -> int:
        if n in self.frog_ans_n:
            return self.frog_ans_n[n]
        else:
            ans = 2 * self.count_frog_jump_way_n(n-1)
            self.frog_ans_n[n] = ans
        return self.frog_ans_n[n]

    """
    题目:我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法
    """
    def cover_rectangle(self, n: int) -> int:
        if n in self.rectangle_map:
            return self.rectangle_map[n]
        else:
            ans = self.cover_rectangle(n-1) + self.cover_rectangle(n-2)
            self.rectangle_map[n] = ans
        return self.rectangle_map[n]

    """
    题目:输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
    """
    def count_one_number_binary(self, n: int) -> int:
        count = 0
        while n:
            n = (n - 1) & n
            count += 1
        return count

    """
    题目:给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
    """
    def power_function(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        temp = 1
        if exponent < 0:
            abs_exponent = -exponent
            while abs_exponent:
                temp = temp * base
                abs_exponent -= 1
            return 1/temp
        while exponent:
            temp = temp * base
            exponent -= 1
        return temp

    """
    题目:输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
         所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    """
    def array_re_order_with_two_extra_array(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for _ in nums:
            if _ % 2 == 0:
                even.append(_)
            else:
                odd.append(_)
        odd.extend(even)
        return odd

    def array_re_order(self, nums: List[int]) -> List[int]:
        size = len(nums)
        p1 = 0
        while p1 < size:
            while nums[p1] % 2 == 1 and p1 < size:
                p1 += 1
            p2 = p1 + 1
            while p2 < size and nums[p2] % 2 == 0:
                p2 += 1
            if p2 < size:
                nums.insert(p1, nums.pop(p2))
                p1 += 1
            else:
                break
        return nums

    def array_re_order_two(self, nums: List[int]) -> List[int]:
        size = len(nums)
        p1 = 0
        temp = []
        while p1 < size:
            while nums[p1] % 2 == 1 and p1 < size:
                p1 += 1
            p2 = p1 + 1
            while p2 < size and nums[p2] % 2 == 0:
                p2 += 1
            if p2 < size:
                temp.extend(nums[p2:])
                temp.extend(nums[:p2])
                nums = temp
            else:
                break
        return nums

    """
    题目:输入一个链表，输出该链表中倒数第k个结点。
    """
    def the_k_node_in_link_list(self, head: ListNode, k: int) -> ListNode or None:
        if not head or k <= 0:
            return None
        p = q = head
        t = 0
        while p and t < k:
            p = p.next
            t += 1
        if t < k:
            return None
        while p is not None:
            p = p.next
            q = q.next
        return q

    """
    题目:反转链表, 请给出两种方式
    """
    def reverse_link_list_iteration(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reverse_link_list_iteration_with_temp_node(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverse_link_list_recursion(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = self.reverse_link_list_recursion(head.next)
        head.next.next = head
        head.next = None
        return tail


    """
    题目:输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
    """
    def combine_two_link_list_with_temp_list(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 若采用临时列表,储存节点值并重新构造
        temp = []
        while l1:
            temp.append(l1.val)
            l1 = l1.next
        while l2:
            temp.append(l2.val)
            l2 = l2.next
        temp.sort()
        size = len(temp)
        if size < 1:
            return None
        head = ListNode(temp[0])
        pre = head
        for i in range(1, size):
            temp_node = ListNode(temp[i])
            pre.next = temp_node
            pre = pre.next
        return head

    def combine_two_link_list_recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.combine_two_link_list_recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.combine_two_link_list_recursion(l1, l2.next)
            return l2
