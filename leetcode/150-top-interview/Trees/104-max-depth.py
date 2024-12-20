# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def loadBFS(a: List[Optional[int]]) -> Optional["TreeNode"]:

        def is_left(node: TreeNode, q: deque) -> bool:
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
        root = TreeNode(a[0])
        q.append(root) # queue will contain parents of the node to be processed, 
        q.append(root) # that is why we put it two times: there will be two nodes to process, L and R
        for item in a[1:]: # starting with 2nd element, since the first is processed already
            parent: TreeNode = q.popleft()
            if item != None:
                curr = TreeNode(item)
                if is_left(parent, q):
                    parent.left = curr
                else:
                    parent.right = curr
                q.append(curr)
                q.append(curr)

        return root            

# solution beats 14%, memory beats 19%
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = deque()
        stack.append([root, 1])
        max_depth = 0
        while stack:
            curr = stack.pop()
            curr_node = curr[0]
            if curr_node.left == None and curr_node.right == None:
                if curr[1] > max_depth:
                    max_depth = curr[1]
            if curr_node.left:
                stack.append([curr_node.left, curr[1]+1])
            if curr_node.right:
                stack.append([curr_node.right, curr[1]+1])
        return max_depth            
        

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
        tree = TreeNode.loadBFS(bfs)
        result = str(tree)
        if result == expected:
            print(f'Test case: {bfs}, passed')
        else:
            print(f'=== Failed: case {bfs}, expected: "{expected}", result: "{result}"')

    test_cases = [
        {
            "BFS": [3,9,20,None,None,15,7], 
            "expected": 3
        },
                {
            "BFS": [1, None, 2], 
            "expected": 2
        },
        {
            "BFS": [1, 2, 3, None, 4, 5, 6, 7, None, None, None, 8, None, None, None, None, 9], 
            "expected": 5
        },
    ]

    for case in range(len(test_cases)):
        root = TreeNode.loadBFS(test_cases[case]['BFS'])
        print(f'=== Test case {case+1}. Input: {str}')
        expected = test_cases[case]['expected']
        s = Solution()
        result = s.maxDepth(root)

        if expected != result:
            print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
        else:
            print(f'Test case {case + 1} passed.  result: {result}')
