"""    Valid Parentheses ==> Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

        Link : https://leetcode.com/problems/find-the-difference/?envType=study-plan-v2&envId=programming-skills

""" 

#  solution (4h)

class Solution(object):

    def isValid(self, s):
        list_s = list(s)
        stack = []

        if list_s.count("(") != list_s.count(")") or list_s.count("{") != list_s.count("}") or list_s.count("[") != list_s.count("]") :
            return False

        opening_bra = ["(", "{" , "["]
        closing_bra = [")" , "}","]"]



        for i , element in enumerate(list_s):
            if element in opening_bra :
                stack.append(element)
                print(f"opening with {element} , {stack}")
            else:
                if stack:
                    if closing_bra.index(element) == opening_bra.index(stack[-1]):
                            print(f"closing {stack[-1] ,opening_bra.index(stack[-1]) } with {element , closing_bra.index(element)} , {stack}")
                            stack.pop(-1)
                    else:
                        return False
                else: 
                    return False
                
            print(stack)
                
        return True

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
result = solution_instance.isValid("[([]])")

# Print the result
print(result)









#       other not working tries

# class Solution(object):

#     def isValid(self, s):
#         list_s = list(s)

#         if list_s.count("(") != list_s.count(")") or list_s.count("{") != list_s.count("}") or list_s.count("[") != list_s.count("]") :
#             return False

#         for i , element in enumerate(list_s):
#             if element == "(":
#                 if ")" not in list_s[i+1:]:
#                     return False
    
#             if element == "{":
#                 if "}" not in list_s[i+1:]:
#                     return False
                
#             if element == "[":
#                 if "]" not in list_s[i+1:]:
#                     return False
#         return True

# class Solution(object):

#     def isValid(self, s):
#         list_s = list(s)
#         list_c = []
#         list_o = []
        

#         if list_s.count("(") != list_s.count(")") or list_s.count("{") != list_s.count("}") or list_s.count("[") != list_s.count("]") :
#             return False


#         opening_bra = ["(", "{" , "["]
#         closing_bra = [")" , "}","]"]


#         bra = ["(" , ")" ,"{" , "}", "[" , "]"]


#         for i , element in enumerate(list_s):
#             if element  in opening_bra :
#                 list_o.append(element) 
#             else:
#                 list_c.append(element)
#                 index_c = list_c.index(element)
#                 index_o = list_o.index(bra[bra.index(element)-1])
#                 if index_o != index_c:
#                     return False
        
#         return True


