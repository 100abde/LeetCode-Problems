
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

 
# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.






class Solution:



    
    def largestRectangleArea(self, heights) -> int:
     
#this must check for each element in the heights 
        def repeated(index):
            value = heights[index] 
            lp , rp = index , index
            rstill , lstill = True ,True
            # print(f"element is {heights[index]} by ====> {index}" )
            while lstill or rstill:
                if lp > 0 and lstill==True:
                    lp -=1
                    if heights[lp] >= heights[index]:
                        # print(f" ===> {heights[lp]} will be added from left by {lp}")
                        value += heights[index]
                        # print(value)
                    else :  lstill=False
                else: 
                    lstill=False

                if rp < len(heights)-1 and rstill==True:
                    rp +=1
                    if heights[rp] >= heights[index]:
                        # print(f" ===> {heights[rp]} will be added from right by {rp}")
                        value += heights[index]
                        # print(value)
                    else :  rstill=False

                else: 
                    rstill= False
            return value


        result = max(heights)

        for i in range(len(heights)):
            x = repeated(i)

            if x > result:
                result = x

        return result



heights = [2,1,5,6,2,3]
heights=[2,4,2,1,1,10]

heights=[2,1,0,2]
object = Solution()
    
print(object.largestRectangleArea(heights))