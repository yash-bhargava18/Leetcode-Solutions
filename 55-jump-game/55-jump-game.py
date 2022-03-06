class Solution:
    def canJump(self, nums: List[int]) -> bool:
        chosen_index = 0
        for index , jump_length in enumerate(nums):
            if chosen_index < index:
                return False
            chosen_index = max(chosen_index, index + jump_length)
        return True