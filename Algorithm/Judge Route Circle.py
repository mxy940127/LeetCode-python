#Author : mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao

'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        origin_x = 0
        origin_y = 0
        for letter in moves:
            if letter == 'R':
                origin_x += 1
            elif letter == 'L':
                origin_x += -1
            elif letter == 'U':
                origin_y += 1
            elif letter == 'D':
                origin_y += -1
            else:
                pass
        if origin_x == 0 and origin_y == 0:
            return True
        else:
            return False