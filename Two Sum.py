#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''




class Solution:
    def twoSum(self, nums, target):
        """
        可以使用两层for循环,但是算法时间复杂度太高,为O(n^2),不考虑。
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #这是两层for循环的解法  5352ms
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        #用一层in方法  1100ms
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums and nums.index(comp) != i:
                return i, nums.index(comp)
        #考虑用map存放比较结果 37ms
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


