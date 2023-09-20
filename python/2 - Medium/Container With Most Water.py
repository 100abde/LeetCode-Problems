"""         Copy List with Random Pointer ==> medium

You are given an integer array height of length n. There are n vertical lines
 drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


    link :https://leetcode.com/problems/container-with-most-water/description/
"""


height = [1,8,6,2,5,4,8,3,7]



class Solution:
    def maxArea(self, height) :
        out = 0
        l , r = 0 , len(height)-1

        while l < r:
            x=(r-l)*min(height[l],height[r])

            if x > out :
                out = x
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return out


# class Solution:
#     def maxArea(self, height) :
#         out = 0
#         for i , elei in enumerate(height):
#             for j , elej in enumerate(height[i+1:]):
#                 x = elej if elej<elei else elei
#                 if abs(x*(j+1) ) > out:
#                     out = abs(x*(j+1) )
#                     print(elei,elej,i,j+1)
#         return out



height = [1,8,6,2,5,4,8,3,7]
# height=[1,1]


# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.maxArea(height)

# Print the result
print(test)