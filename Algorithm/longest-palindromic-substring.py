#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao


'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''


# class Solution:
#
#     def longestPalindrome(self, s: str) -> str:
#         #store[i][j]储存s从i到j组成的字符串是否为回文
#
#         #初始化 dp 全为false
#         size = len(s)
#         dp = [[False for _ in range(size)] for _ in range(size)]
#
#         #斜对角线 i=j 为true
#         for i in range(size):
#             dp[i][i] = True
#
#         for i in range(size):
#             for j in range(0, i):
#                 if s[i] == s[j]:
                    

if __name__ == '__main__':
    # s = Solution()
    # print(s.longestPalindrome("abcd"))
    pass