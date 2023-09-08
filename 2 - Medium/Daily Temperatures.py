"""         Daily Temperatures ==> medium

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait
 after the ith day to get a warmer temperature. If there is no future day for which
   this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
    link : https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=daily-question&envId=2023-09-05
"""

#this was my code but it turneds out that Its has a complexity of O( n² ) 


#  class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         holder = [0]*len(temperatures)
#         out = [0]*len(temperatures)
#         modified = [False]*len(temperatures)

#         for i , element in enumerate(temperatures):
#             if i<=  len(temperatures)-1:
#                 for x , x_ele  in enumerate(temperatures[:i]):
#                     if not modified[x]:
#                         holder[x]+=1
#                         if element > x_ele: 
#                             modified[x]= True
#                             out[x] = holder[x]
#             else:
#                 out[i]=0


#         return out


#code of O( n )

class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result

temperatures = [73,74,75,71,69,72,76,73]

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.dailyTemperatures(temperatures)

# Print the result
print(test)