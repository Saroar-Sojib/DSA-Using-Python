class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

class Solution:
    def isBalanced(self, root):
        self.flag = True
        def dfs(root):
            if not root:
                return 0
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            if abs(left_node-right_node)>1:
                self.flag = False
                return -1
            return 1+max(left_node,right_node)
         
        dfs(root)
        return self.flag 


if __name__ == '__main__':
    '''
                3                          
              /   \  
            9      20 
                   / \     
                  15   7   

    '''
    Tree = Node(3)
    Tree.left = Node(9)
    Tree.right = Node(20)
    Tree.right.left = Node(15)
    Tree.right.right = Node(7)
    
    ans = Solution()
    print(ans.isBalanced(Tree))