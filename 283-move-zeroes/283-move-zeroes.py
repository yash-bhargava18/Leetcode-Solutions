class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start] == 0:
                nums.pop(start)
                nums.append(0)
                end -= 1
            else:
                start += 1
            
            
                    