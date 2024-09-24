from math import floor
from typing import List


class Solution:
  
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       nums =nums1+nums2
       num=sorted(nums)
       mid = floor(len(num)/2)
       if len(nums)%2!=0:
          print(num[mid])
          return num[mid]
          
       else:
            print(num[mid-1]/2+num[mid]/2)
            return (num[mid-1]/2+num[mid]/2)  
solution=Solution()        
rezultat=solution.findMedianSortedArrays([1,2],[3,4])   
print(rezultat)       