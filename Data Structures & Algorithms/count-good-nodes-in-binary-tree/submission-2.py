# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append((root, float("-inf")))

        while q:
            node, max_val = q.popleft()
            print(f"Current node and max_val: {node.val} {max_val}")
            if node.val >= max_val:
                res += 1
                print(f"Max val exceeds node val, res up to {res}")
            if node.left:
                q.append((node.left, max(node.val, max_val)))
            if node.right:
                q.append((node.right, max(node.val, max_val)))

        return res


        

    


"""
parent_dict = {
    2: None,
    1: 2,
    1: 2,

}

"""