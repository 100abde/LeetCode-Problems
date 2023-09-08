"""        Contains Duplicate ==> Medium


Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
 You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
    Link :https://leetcode.com/problems/top-k-frequent-elements/

"""

                        #My Solution


from itertools import chain

class Solution(object):
    def topKFrequent( self ,nums, k):
        dic = {}
        while nums != []:
            if nums.count(nums[-1]) not in dic:
                dic[nums.count(nums[-1])] = [nums[-1]]
            else:
                dic[nums.count(nums[-1])].append(nums[-1])  
            nums = [element  for element in nums if element != nums[-1] ]

        shows = list(dic.keys())
        for i in range(k):
            if shows:
                nums.append(dic.get(max(shows)))
                shows.remove(max(shows))
        return list(chain(*nums))[:k]
        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.topKFrequent([1,1,1,2,2,3],  2)

# Print the result
print(result)