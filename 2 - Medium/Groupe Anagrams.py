"""        Group Anagrams ==> Medium

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


    Link : https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

"""

                        #My Solution


class Solution(object):
    def groupAnagrams(self, strs):
            # categories = []
            # ret= []
            # for i in strs:
            #     if Counter(i) not in categories:
            #         categories.append(Counter(i))
            #         ret.append([ element for element in strs if Counter(element)==Counter(i) ])
            # return ret     "time limited"

            diction = {}
            for element in strs:
                if tuple(sorted(element)) not in diction:
                    diction[tuple(sorted(element))]=[element]
                else:
                    diction[tuple(sorted(element))].append(element)
            return diction.values()

        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

# Print the result
print(result)