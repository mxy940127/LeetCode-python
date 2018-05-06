#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao
'''
给出了两个A和B的列表，从A映射到B，B是由A的一种回文构词法构成通过随机化A中元素的顺序来实现的。
我们想要找到一个指数映射P，从A到B，映射P[i] = j表示A出现在B中的第i个元素。
这些列表A和B可能包含重复。如果有多个答案，输出任何一个。
注意事项:
A,B的数组长度相等，范围[1,100]。
A[i],B[i]是整数范围[0, 10^5]。
'''

class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        '''
        :param A:
        :param B:
        :return:
        '''
        list = []
        for i in A:
            list.append(B.index(i))
        return list