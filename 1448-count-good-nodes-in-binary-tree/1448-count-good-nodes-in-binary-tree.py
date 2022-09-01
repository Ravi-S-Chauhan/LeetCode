# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode,ma = -100000) -> int:
        return self.goodNodes(root.left,max(root.val,ma))+self.goodNodes(root.right,max(root.val,ma))+ (root.val>=ma) if root else 0