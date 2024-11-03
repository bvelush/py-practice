# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional

# Definition for singly-linked list.

# Accepted
# 4420ms
# Beats 6.63%of users with Python3
# Memory
# Details
# 20.89MB
# Beats 19.27%of users with Python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list2str(self, delimiter) -> str:
        '''
        Converting a list until next is None (no check for circular lists) to string of the following format:
        val(delimiter)val, for example, .print(' => ') would result in val => val

        '''
        ret_val = ''
        curr = self
        while True:
            ret_val += str(curr.val)
            if not curr.next:
                break
            curr = curr.next
            ret_val += delimiter
        
        return ret_val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = [lists[i] for i in range(len(lists))]
        ret_val = ListNode(0) # this head will be removed later, right now I need it to avoid cluttering NULL checks
        ret_val_curr = ret_val
        while True:
            min_pointer = self._min_pointer(pointers)
            if min_pointer == None:
                break
            ret_val_curr.next = ListNode(pointers[min_pointer].val)
            pointers[min_pointer] = pointers[min_pointer].next
            ret_val_curr = ret_val_curr.next
        
        return ret_val.next # cutting out the fictious head


    def _min_pointer(self, pointers: List[Optional[ListNode]]) -> Optional[int]:
        min_val = 1000000000000
        all_pointers_null = True
        for i in range(len(pointers)):
            if not pointers[i]:
                continue
            all_pointers_null = False
            if min_val > pointers[i].val:
                min_val = pointers[i].val
                ret_val = i

        if all_pointers_null:
            return None
        return ret_val


S = Solution()
input = [
    ListNode(1, ListNode(4, ListNode(5))), 
    ListNode(1, ListNode(3, ListNode(4))), 
    ListNode(2, ListNode(6))
]
for i in range(len(input)):
    print(input[i].list2str(' => '))

output_list = S.mergeKLists(input)
print(output_list.list2str('->'))

