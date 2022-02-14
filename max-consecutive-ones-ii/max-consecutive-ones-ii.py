class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sequence = 0
        left = 0
        right = 0
        num_zeroes = 0
        
        while right < len(nums):
            
            if nums[right] == 0:
                num_zeroes += 1
            
            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            
            sequence = max(sequence, right - left + 1)
            right += 1
            
        return sequence
                
                
                