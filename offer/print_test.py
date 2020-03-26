print(3&1)

from offer.offer_solution import *

A1 = ListNode(1)
A2 = ListNode(3)
A3 = ListNode(5)
A4 = ListNode(7)
A5 = ListNode(9)
A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5
A5.next = None

B1 = ListNode(2)
B2 = ListNode(4)
B3 = ListNode(6)
B4 = ListNode(8)
B5 = ListNode(10)
B1.next = B2
B2.next = B3
B3.next = B4
B4.next = B5
B5.next = None

s = Solution()
c = s.combine_two_link_list_recursion(A1, B1)
print(s.combine_two_link_list_recursion(A1, B1))