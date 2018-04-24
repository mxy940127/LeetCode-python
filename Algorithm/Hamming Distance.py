#Author : mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        c = 0
        while z > 0:
            if z & 1 == 1:  # 说明当前一位为1
                c += 1
            z = z >> 1
        return c


