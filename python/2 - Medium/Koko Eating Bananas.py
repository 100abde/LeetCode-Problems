""""        Koko Eating Bananas  ==> Meduim

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile 
of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats 
all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 
        Link : https://leetcode.com/problems/koko-eating-bananas/description/

"""

import math

class Solution:
    def minEatingSpeed(self, piles , h ):
        final = max(piles)
        def out(k):
            res = 0
            i=0 
            while len(piles) > i :
                res +=  math.ceil(piles[i]/k)
                i+=1
            return res

        l , r = 1 , max(piles)

        while l<=r:
            m = (l+r)//2
            print(l ,r , final)
            x = out(m)

            if x > h :  
                l = m + 1
            else  :

                final = min(final, m)
                r = m - 1
        return final

piles = [30,11,23,4,20]
h = 6

piles = [3,6,7,11]
h = 8

# piles = [312884470]
# h = 312884469

piles = [312884470]
h = 968709470

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.minEatingSpeed(piles , h)

# Print the result
print(test)