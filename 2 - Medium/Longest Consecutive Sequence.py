"""        Product of Array Except Self ==> Medium

Given an integer array nums, return an array answer such that answer[i] is
 equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

    Link : https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150

"""

                        #My Solution


import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):
        awnser = np.array([1]*len(nums))
        for i ,element in enumerate(nums):
            holder = awnser[i]
            awnser = awnser*element
            awnser[i] = holder
        return awnser
         
        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.productExceptSelf([-1,1,0,-3,3])

# Print the result
print(result)