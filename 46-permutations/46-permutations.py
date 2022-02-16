class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.depth_first(nums,[],result)
        return result
    
    def depth_first(self,nums,path,result):
        if not nums:
            result.append(path)
        for i in range(len(nums)):
            self.depth_first(nums[:i] + nums[i+1:], path + [nums[i]],result)