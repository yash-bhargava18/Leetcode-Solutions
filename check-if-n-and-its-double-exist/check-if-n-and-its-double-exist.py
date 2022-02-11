class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        arr_set = set()
        for i in arr:
            if i*2 in arr_set:
                return True
            elif i % 2 == 0 and i // 2 in arr_set:
                return True
            else:
                arr_set.add(i)
                
        return False
        