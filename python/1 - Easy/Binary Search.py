"""             Binary Search ==>   Easy


Given an array of integers nums which is sorted in ascending order, and 
an integer target, write a function to search target in nums. If target
 exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


    Link : https://leetcode.com/problems/binary-search/description/

"""



class Solution:
    def minOperations(self, nums , target):
        l , r = 0 , len(nums)-1
        if target < nums[l] or target > nums[r] :
            return -1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m -1
            else :
                return m
        return -1
    
nums = [-1,0,3,5,6,7,8,9,12]
target = 9

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.minOperations(nums,target)

# Print the result
print(test)

