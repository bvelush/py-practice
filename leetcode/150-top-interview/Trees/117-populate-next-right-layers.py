# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self) -> str: # printing with DFS, preprocess, Left first
        ret_val = ''
        stack = deque()
        stack.append(self)
        while stack:
            curr = stack.pop()
            if curr:
                ret_val += f'{curr.val}, '
                stack.append(curr.right)
                stack.append(curr.left)
            else:
                ret_val += f'N, '
        return ret_val

    @staticmethod
    def loadBFS(a: List[Optional[int]]) -> Optional["Node"]:

        def is_left(node: Node, q: deque) -> bool:
            '''
                Check for node equality to the next node. In this context, if they are equal, 
                then the node is left to its parent, otherwise -- right
            '''
            next = None
            if q:
                next = q[0]
            return node == next

        if len(a) == 0:
            return None
        q = deque()
        root = Node(a[0])
        q.append(root) # queue will contain parents of the node to be processed, 
        q.append(root) # that is why we put it two times: there will be two nodes to process, L and R
        for item in a[1:]: # starting with 2nd element, since the first is processed already
            parent: Node = q.popleft()
            if item != None:
                curr = Node(item)
                if is_left(parent, q):
                    parent.left = curr
                else:
                    parent.right = curr
                q.append(curr)
                q.append(curr)

        return root            

# Solution 1: beats 56%, memory beats 7%
# for each item in queue, we store the 'level'. when level is the same, we connect nodes at the same level
class Solution1:
        def connect(self, root: 'Node') -> 'Node':

            def peek(q: deque) -> Node:
                if q:
                    return q[0]
                else: 
                    return None

            if root == None:
                return None
            q = deque()
            q.append([root, 0])
            while q:
                curr = q.popleft()
                curr_node = curr[0]
                curr_level = curr[1]
                next_node = peek(q)
                if next_node:
                    if curr_level == next_node[1]:
                        curr_node.next = next_node[0]
                if curr_node.left:
                    q.append([curr_node.left, curr_level+1])
                if curr_node.right:
                    q.append([curr_node.right, curr_level+1])

            return root
        
# solution 2: the idea is that at each level the queue contains only this level elements. So if we iterate for len(queue), 
# for each element until the last setting next, and adding its children to the queue (but size will not change if it's in variable)
# then we can speed up the process
class Solution:
        def connect(self, root: 'Node') -> 'Node':
            if root == None:
                return None

            q = deque()
            q.append(root)

            return root

if __name__ == "__main__":

    test_loadBFS = [
        {
            "BFS": [], 
            "expected": "None"
        },
        {
            "BFS": [1], 
            "expected": "1, N, N, "
        },
        {
            "BFS": [3,9,20,None,None,15,7], 
            "expected": "3, 9, N, N, 20, 15, N, N, 7, N, N, "
        },
        {
            "BFS": [1, 2, 3, None, 4, 5, 6, 7, None, None, None, 8, None, None, None, None, 9], 
            "expected": "1, 2, N, 4, 7, N, N, N, 3, 5, N, N, 6, 8, N, 9, N, N, N, "
        },
    ]

    for case in test_loadBFS:
        bfs = case["BFS"]
        expected = case["expected"]
        tree = Node.loadBFS(bfs)
        result = str(tree)
        if result == expected:
            print(f'Test case: {bfs}, passed')
        else:
            print(f'=== Failed: case {bfs}, expected: "{expected}", result: "{result}"')

    test_cases = [
        {
            "BFS": [1,2,3,4,5,None,7], 
            "expected": [1,'#',2,3,'#',4,5,7,'#']
        },
        {
            "BFS": [], 
            "expected": []
        },
        # {
        #     "BFS": [1, 2, 3, None, 4, 5, 6, 7, None, None, None, 8, None, None, None, None, 9], 
        #     "expected": 5
        # },
    ]

    for case in range(len(test_cases)):
        root = Node.loadBFS(test_cases[case]['BFS'])
        print(f'=== Test case {case+1}. Input: {str}')
        expected = test_cases[case]['expected']
        s = Solution()
        result = s.connect(root)

        if expected != result:
            print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
        else:
            print(f'Test case {case + 1} passed.  result: {result}')
