class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(i, amount):
            if amount == 0:
                return 0
            if i == len(coins):
                return math.inf
            
            mincoins = dp(i+1, amount)  
            if amount >= coins[i]:  
                mincoins = min(mincoins, dp(i, amount - coins[i]) + 1)
            return mincoins
        
        mincoins = dp(0, amount)
        if mincoins != math.inf:
            return mincoins
        else:
            return -1