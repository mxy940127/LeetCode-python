#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao

from offer.offer_solution import Solution, ListNode

s = Solution()


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