"""        Valid Anagram ==> Easy

    Given two strings s and t, return true if t is an anagram of s,
    and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false


    Link : https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=programming-skills

"""

                        #My Solution


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s.count(s[i]) != t.count(s[i]):
                return False
        return True
        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.isAnagram("rat", "car")

# Print the result
print(result)