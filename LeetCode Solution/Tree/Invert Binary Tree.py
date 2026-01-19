class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def PrintTree ( self ) :
       if self.left :
           self.left.PrintTree ()
       print ( self.data, end= ' ' ) ,
       if self.right :
           self.right.PrintTree ()

class Solution:
    def invertTree(self, root):
        def dfs(root):
            if root is None:
                return None
            dfs(root.left)
            dfs(root.right)
            root.left,root.right=root.right,root.left
            return root
        dfs(root)
        return root

if __name__ == '__main__':
    '''
                4                                             4
              /   \                                          /  \           
            2      7              ========>>                7    2           
           / \    / \                                      / \   / \
          1   3   6  9                                    9   6  3  1

    '''
    Tree = Node(4)
    Tree.left = Node(2)
    Tree.right = Node(7)
    Tree.left.left = Node(1)
    Tree.left.right = Node(3)
    Tree.right.left = Node(6)
    Tree.right.right = Node(9)
    print('Initial Tree :',end = ' ' )
    Tree.PrintTree()
    Solution().invertTree(root=Tree)
    print('\nInverted Tree :', end=' ')
    Tree.PrintTree()
    print()
