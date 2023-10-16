""""        Generate Parentheses ==> Medium

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
    
        link : https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution:
    def generateParenthesis(self, n):
        final = []
        option =[]
        

        def test(open , close  ):
            if open == close == n :
                final.append("".join(option))
                return
            
            if close < open :
                option.append(')')
                test(open , close+1  )
                option.pop()

            if open < n :
                option.append('(')
                test(open+1 , close )
                option.pop()

        test(0, 0 )
        
        return final
    
n = 9

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.generateParenthesis(n)

# Print the result
print(test)