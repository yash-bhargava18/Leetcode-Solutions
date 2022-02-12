class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = x
            x = max(x,temp)
        return arr
                
                
        
            