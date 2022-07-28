class Solution:
    def findMin(self, nums) -> int:
        left,right=0,len(nums)-1
        mid=(left+right)//2
        while right-left>1:
            if nums[mid]>nums[left]:
                if nums[mid]<nums[right]:
                    right=mid-1         #case2
                else:
                    left=mid+1          #case1   
            else:
                right=mid               #case3
            mid=(left+right)//2
        return min(nums[mid],nums[right])
        