class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        low = 0
        high = size - 1
        
        if(len(nums) == 0):
            return -1
        
        while(low <= high):
            mid = low + (high - low) // 2
            if(nums[mid] == target):
                return mid
        
            elif(nums[low] <= nums[mid]):
                #condition if left side is sorted
                if(nums[low] <= target and nums[mid] > target):
                    high = mid - 1
                else:
                    low = mid+1
            else:#condition for right side sorted
                if(nums[mid] < target and nums[high] >= target):
                    low = mid+1
                else:
                    high = mid-1
        
        return -1
                