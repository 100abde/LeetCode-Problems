""""            Search a 2D Matrix  ==> medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


class Solution:
    def searchMatrix(self, matrix, target):
        t , b  = 0 , len(matrix) - 1
        l , r  = 0 , len(matrix[0]) - 1

        while t <= b :
            print("While 1")
            m = (t + b)//2
            print(t , m , b)
            print( matrix[m][l], target , matrix[m][r] )
            if matrix[m][l] <= target <= matrix[m][r]:
                line = m 
                while l<=r :
                    print("While 2")

                    m = (l+r)//2
                    print(l, m , r)
                    if matrix[line][m] == target : 
                        return True
                    
                    elif matrix[line][m] < target :
                        l = m + 1

                    elif matrix[line][m] > target :
                        r = m - 1
                return False
            elif matrix[m][l] > target :
                b = m - 1
            elif matrix[m][r] < target :
                t = m +1

        return False



matrix = [[1,2,3,4,5,7],[10,11,12 , 13 ,16,20],[23 , 24 , 26,30,34,60]]
target = 61     

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.searchMatrix(matrix,target)

# Print the result
print(test)



# nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

# print(nums[2][0])



# class Solution:
#     def searchMatrix(self, matrix, target):
#         h , l = 0 , len(matrix)-1
#         i=0

#         while h<l:
#             m = h + ((l-h)//2)
#             print(f'while 1 ')
#             i +=1
#             print(h,m,l)
#             print(matrix[m][0],target , matrix[m][len(matrix[0])-1])
#             if matrix[m][0] <= target <= matrix[m][len(matrix[0])-1]:
#                 line = m
#                 l , r = 0 , len(matrix[0])-1

#                 while l<r:
#                     print(f'while 2 ')
#                     print(line , matrix[line][l],matrix[line][r] , matrix[line])
#                     if matrix[line][l] == target or matrix[line][r]==target:
#                         return True
                    
#                     m = l+((r-l)//2)
#                     print(l,m,r)
#                     print(target , matrix[line][m])

#                     if target < matrix[line][m]:
#                         r = m -1
#                     elif target > matrix[line][m]:
#                         l = m +1
#                     else :
#                         return True
#                 return False
#             elif matrix[m][0] > target :
#                 l = m -1
#             elif matrix[m][len(matrix[0])-1] < target :
#                 h = m +1
#             print(h,m,l)


#         return False