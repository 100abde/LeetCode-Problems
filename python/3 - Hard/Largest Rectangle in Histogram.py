"""""   Largest Rectangle in Histogram ==>

Given an array of integers heights representing the histogram's bar height where the width
 of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


    Link : https://leetcode.com/problems/largest-rectangle-in-histogram/
 """

#it wont be submited in  leetcode  , i faced the time limeted error , but i'll come back to it


class Solution(object):

    def largestRectangleArea(self, heights):
        score = max(heights)

        for i, element in enumerate(heights):
            pointer = 0

            x = [element<= ele  for ele in heights[i:] ]
            z = heights[:i]
            z.reverse()
            y = [element<= ele  for ele in z ]
                
            i,j=0 ,0   
            if x:
                while len(x) > i and x[i]:
                    pointer+=1
                    i+=1
            if y:
                while len(y)>j and y[j]:
                    pointer+=1
                    j+=1
            
            if score< pointer*element:
                score=pointer*element
        return score


heights = [2,1,2]
heights = [2,1,5,6,2,3]
  
# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.largestRectangleArea(heights)

# Print the result

print(test)

            

# class Solution(object):

#     def largestRectangleArea(self, heights):

#         highest_histogram = heights[0] 
#         length = min(heights)*len(heights)

#         for i , element in enumerate(heights[1:]):
#             if element >= heights[i] :
#                 x = heights[i] *2
#             else:
#                 x= element*2

#             if x > highest_histogram:
#                 highest_histogram = x

#             if element > highest_histogram:
#                 highest_histogram = element
#         if highest_histogram > length:
#             return highest_histogram
#         else:
#             return length
    