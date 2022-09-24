# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def solve(root,sm,temp,result):
            if root:
                if not root.left and not root.right and sm == root.val:
                    temp.append(root.val)
                    result.append(temp)
                    return
                solve(root.left,sm-root.val,temp+[root.val],result)
                solve(root.right,sm-root.val,temp+[root.val],result)
        result = []
        solve(root,targetSum,[],result)
        return result
        