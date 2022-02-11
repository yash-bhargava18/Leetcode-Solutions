class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        j = len(arr)
        i = 0
        
        while i+1 < j and arr[i] < arr[i+1]:
            i += 1
        if i == 0 or i == j-1:
            return False
        while i+1 < j and arr[i] > arr[i+1]:
            i += 1
        if i == j-1:
            return True
        
        return False
            