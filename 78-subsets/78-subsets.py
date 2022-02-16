class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def explore(chosen_element, remaining_element, result):
            if not remaining_element:
                result.append(chosen_element[:])
                return
            d = remaining_element.pop(0)
            chosen_element.append(d)
            explore(chosen_element, remaining_element, result)
            chosen_element.pop()
            explore(chosen_element, remaining_element, result)
            remaining_element.insert(0, d)
        
        result = []
        chosen_element = []
        explore(chosen_element, nums, result)
        return result
            