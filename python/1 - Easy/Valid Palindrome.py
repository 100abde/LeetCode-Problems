"""        Valid Palindrome ==> Easy
 

A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. Alphanumeric characters
   include letters and numbers.

Given a string s, return true if it is a palindrome, or false
 otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
    Link :https://leetcode.com/problems/contains-duplicate/

"""

                        #My Solution


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
    
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        # word = ''.join([(s.lower())[i] for i in range(len(s)) if  48<=ord((s.lower())[i]) <= 57 or 97<=ord((s.lower())[i]) <= 122 ])
        
        # for i in range(int(len(word)/2)):
        #     if word[i] != word[-1-i]:
        #         return False
            
        # return True
    
s = "A man, a plan, a canal: Panama"  
s = "race a car"  
s='0P'
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.isPalindrome(s)

# Print the result
print(result)

