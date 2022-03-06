class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        var1 = sum(nums)
        if var1 % 2 != 0:
            return False
        var1 = var1 // 2
        
        dp = [False] * (var1 + 1)
        dp[0] = True
        
        for i in nums:
            for j in range(var1,i-1,-1):
                if dp[var1]:
                    return True
                dp[j] = dp[j] or dp[j - i]
        return dp[var1]