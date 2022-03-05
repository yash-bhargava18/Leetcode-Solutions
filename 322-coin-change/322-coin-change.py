class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(i, amount):
            if amount == 0:
                return 0
            if i == len(coins):
                return math.inf
            
            ans = dp(i+1, amount)  # Skip ith coin
            if amount >= coins[i]:  # Used ith coin
                ans = min(ans, dp(i, amount - coins[i]) + 1)
            return ans
        
        ans = dp(0, amount)
        if ans != math.inf:
            return ans
        else:
            return -1