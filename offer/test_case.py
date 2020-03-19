#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao

from offer.offer_solution import Solution, ListNode
from offer.queue import MyQueue

s = Solution()

q = MyQueue()

def test_find_in_two_dimensional_arrays():
    arrays = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert s.find_in_two_dimensional_array(arrays=arrays, target=1) is True
    assert s.find_in_two_dimensional_array(arrays=arrays, target=0) is False
    assert s.find_in_two_dimensional_array(arrays=[[]], target=2) is False
    assert s.find_in_two_dimensional_array(arrays=[], target=2) is False


def test_binary_search_in_two_dimensional_arrays():
    arrays = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert s.binary_search_in_two_dimensional_array(arrays=arrays, target=13) is True
    assert s.binary_search_in_two_dimensional_array(arrays=arrays, target=0) is False
    assert s.binary_search_in_two_dimensional_array(arrays=[[]], target=2) is False
    assert s.binary_search_in_two_dimensional_array(arrays=[], target=2) is False


def test_replace_blank():
    string = "We Are Happy"
    assert s.replace_blank(string=string) == "We%20Are%20Happy"


def test_reverse_linkedlist():
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    A5 = ListNode(5)
    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5
    A5.next = None

    assert s.reverse_linklist_and_print(A1) == [5, 4, 3, 2, 1]


def test_reconstruct_binary_tree():
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    assert s.reConstructBinaryTree(pre, tin).val == 1
    assert s.reConstructBinaryTree(pre, tin).left.val == 2


def test_queue_function():
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False


def test_rotate_part_of_arrays():
    assert s.rotate_part_of_array(nums=[3, 4, 5, 1, 2]) == 1
    assert s.rotate_part_of_array(nums=[1, 3, 5, 7, 9]) == 1


def test_fib_arrays():
    import random
    n = random.randint(30, 100)
    assert s.fib_bottom_up(n) == s.fib_up_down(n)


def test_count_frog_jump_way():
    n = 6
    assert s.count_frog_jump_way(n) == 13


def test_count_frog_jump_way_n():
    n = 6
    assert s.count_frog_jump_way_n(n) == 2**(n-1)


def test_cover_rectangle():
    n = 6
    assert s.cover_rectangle(n) == 13


def test_one_bits_in_number():
    n = 9
    assert s.count_one_number_binary(n) == 2