"""        Contains Duplicate ==> Easy



Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
    Link :https://leetcode.com/problems/contains-duplicate/

"""

                        #My Solution


# class Solution(object):
#     def containsDuplicate(self, nums):
#         for i in nums:
#             if nums.count(i)>1 :
#                 return True
#         return False


class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
        return False
         
        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.containsDuplicate([1,2,3,4])

# Print the result
print(result)