"""        Merge Strings Alternatley ==> Easy

    You are given two strings "word1" and "word2". 

    Merge the strings by adding letters in alternating order, 
    starting with "word1". If a string is longer than the other, 
    append the additional letters onto the end of the merged string.

    Return the merged string.

    Example 1:

    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r


    Link : https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=programming-skills

"""

                        #My Solution


class Solution(object):
    def mergeAlternately(self, word1, word2):
        out = ''                        #the output
        min = 0                         # pointer for the small word  

        if len(word1) < len(word2):     #Defining the smallest word
            min = 1

        # Merging elemnts from Word1 and Word2 for len(smallest word)

        for i in range(len(word1 if min== 1 else word2)):
            out = out + word1[i] + word2[i]

        #Adding the rest 

        out= out + (word1[len(word2):] if min != 1 else word2[len(word1):])
        
        return out
        
        
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.mergeAlternately("abc", "pqr")

# Print the result
print(result)