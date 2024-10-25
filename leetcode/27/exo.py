class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        h=0 
        a=len(nums)
        for i in range(a):
            if nums[i]==val:
              nums[i]='_'
              nums[len(nums)-1]=val
              a=-1  
            else:
                h=+1     
        return len(nums) , nums         
              