class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

class Solution:
    def diameterOfBinaryTree(self,root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            res[0] = max(res[0],left_node+right_node+2)
            return 1+max(left_node,right_node)
        dfs(root)
        return res[0]


if __name__ == '__main__':
    '''
                1                          
              /   \  
            2      3 
           / \     
          4   5   

    '''
    Tree = Node(1)
    Tree.left = Node(2)
    Tree.right = Node(3)
    Tree.left.left = Node(4)
    Tree.left.right = Node(5)
    
    ans = Solution()
    print(ans.diameterOfBinaryTree(Tree))