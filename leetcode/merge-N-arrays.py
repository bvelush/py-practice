# merge K sorted lists to a single list (N is the length of longest list)
# assumption is that sublists are non-empty
# I didn't find this problem on leetcode, but decided it would be an interesting thing to solve. 
# Complexity: O(K * N), Memory: O(all elements of Lists)
from typing import List

class Solution:
    def merge(self, lists: List[List[int]]) -> List[int]:
        if not lists:
            return []
        pointers = [0 for _ in range(len(lists))]
        ret_val = []
        while True:
            min_pointer_index = self._find_min_pointer_index(lists, pointers)
            if min_pointer_index < 0:
                break
            item_to_append = lists[min_pointer_index][pointers[min_pointer_index]]
            ret_val.append(item_to_append)
            pointers[min_pointer_index] += 1
            if pointers[min_pointer_index] >= len(lists[min_pointer_index]):
                pointers[min_pointer_index] = -1

        return ret_val

    def _find_min_pointer_index(self, lists: List[List[int]], pointers: List[int]) -> int:
        '''
        returns the index of the sublist in lists with the minimal element
        if pointer is -1, then it must be skipped
        returns -1 if all pointers are out of range
        '''
        min_val = 1000000000000
        all_pointers_out_of_range = True
        for p in range(len(pointers)):
            if pointers[p] < 0:
                continue
            all_pointers_out_of_range = False
            if lists[p][pointers[p]] < min_val:
                min_val = lists[p][pointers[p]]
                ret_val = p
        
        if all_pointers_out_of_range: 
            return -1
        return ret_val
    
S = Solution()

lists = [
    [1, 6], 
    [0, 1, 2, 7, 9], 
    [3, 4, 5, 6]
]

assert(S._find_min_pointer_index(lists, [0, 0, 0]) == 1)
assert(S._find_min_pointer_index(lists, [0, 1, 0]) == 0)
assert(S._find_min_pointer_index(lists, [1, -1, 2]) == 2)
assert(S._find_min_pointer_index(lists, [-1, -1, -1]) == -1)

assert(S.merge(lists) == [0, 1, 1, 2, 3, 4, 5, 6, 6, 7, 9])