# 22. Generate Parentheses
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:

# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int):
        Parentheses = []
        element = ""
        def tracking( open , close , element:str):

            
            if open == close == n :
                Parentheses.append(element)
                return
        
            if open < n :
                tracking( open +1 , close , element + "(")

            if close < open:

                tracking( open  , close + 1 , element  + ")")     
    
        tracking(0,0 , element)
        return Parentheses

test = Solution()

print(test.generateParenthesis(3))