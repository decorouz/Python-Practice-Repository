"""Given a binary tree, determine whether or not it is height-balanced.

A height-balanced binary tree can be defined as one in which the heights 
of the two subtrees of any TreeNode never differ by more than one.
"""


class TreeNode:
    """Base class representing a tree node."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Check if binary tree is balanced."""

    def is_balanced(self, node):
        """Determine if binary tree is balanced.

        Parameters
        ----------
        node:
            A node of the binary tree

        Return
        ------
        bool
            True if balanced else False

        """
        # base case: if node is None, the tree is balanced and has height 0
        if node is None:
            return True, 0

        left = self.is_balanced(node.left)
        right = self.is_balanced(node.right)

        left_s = left[0]
        right_s = right[0]

        # check the difference in heights of left and right subtrees
        diff = abs(left[1] - right[1]) <= 1

        if left_s and right_s and diff:
            return True, max(left[1], right[1]) + 1

        # otherwise, the tree is not balanced
        return False, 0


# Driver Code
if __name__ == "__main__":
    # create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    # create an object of the Solution class
    obj = Solution()
    if obj.is_balanced(root)[0]:
        print("True: Balanced binary tree")
    else:
        print("False: Binary tree not balanced")
