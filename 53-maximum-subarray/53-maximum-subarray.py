class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = 0
        result = nums[0]
        for i in nums:
            if sum1 > 0:
                sum1 += i
            else:
                sum1 = i
            result = max(sum1, result)
        return result