class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pos_dups = 0
        arr_len = len(arr) - 1
        
        for i in range(len(arr)):
            if i > arr_len - pos_dups:
                break
                
            if arr[i] == 0:
                if i == arr_len - pos_dups:
                    arr[arr_len] = 0
                    arr_len -= 1
                    break
                pos_dups += 1
        
        j = arr_len - pos_dups
        for i in range(j,-1,-1):
            if arr[i] == 0:
                arr[i + pos_dups] = 0
                pos_dups -= 1
                arr[i + pos_dups] = 0
            else:
                arr[i + pos_dups] = arr[i]
                
            
                