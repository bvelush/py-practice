# TODO: what is this code? there are syntactic errors, review

# class TreeNode:

#     def __init__(self: 'TreeNode', value: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
#         self.val = value
#         self.left = left
#         self.right = right

#     def dfs_recursive_inorder(self: 'TreeNode', node: 'TreeNode' = None, action: 'method' = print) -> None:
#         if not node:
#             node = self
#         if node.left:
#             self.dfs_recursive_inorder(node.left, action)
#         action(node.val)
#         if node.right:
#             self.dfs_recursive_inorder(node.right, action)

#     def dfs_iterative_inorder(self: 'TreeNode', action: 'method' = print) -> None:
#         s = []
#         s.append(self)
#         if self.left:
#             s.append(left)

#         while s.count() > 0:


# t = TreeNode(1,
#              TreeNode(2,
#                       TreeNode(3),
#                       TreeNode(4)),
#              TreeNode(5,
#                       None,
#                       TreeNode(6)))


# t.dfs_recursive_inorder()

# a = []
# a.append(1)
# a.append(2)
# print(a.pop())
# print(a.pop())
