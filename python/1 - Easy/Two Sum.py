"""        Two Sum ==> Easy

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


    Link : https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
"""

                        #My Solution


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:

                if nums.index(target - nums[i]) != i:
                    return [i , nums.index(target-nums[i])]
                else:
                    return [i , nums[i+1:].index(target-nums[i])+i+1]

        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.twoSum([2,7,11,15],  9)

# Print the result
print(result)