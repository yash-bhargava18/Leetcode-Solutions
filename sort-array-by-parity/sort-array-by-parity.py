class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        
        while left < right:
            if nums[left] % 2 != 0:
                if  nums[right] % 2 == 0:
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return nums