class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

class Solution:
    def maxDepth(self, root):
        ans = 0
        temp_list = []
        temp_list.append(root)
        while(temp_list):
            temp_len=len(temp_list)
            for i in range(temp_len):
                node = temp_list.pop(0)
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            ans+=1
        return ans 
        # def dfs(root):
        #     if root is None:
        #         return 0
        #     return 1+max(dfs(root.left),dfs(root.right))
        # return dfs(root)
    
if __name__ == '__main__':
    '''
                4                          
              /   \  
            2      7 
           / \    / \ 
          1   3   6  9

    '''
    Tree = Node(4)
    Tree.left = Node(2)
    Tree.right = Node(7)
    Tree.left.left = Node(1)
    Tree.left.right = Node(3)
    Tree.right.left = Node(6)
    Tree.right.right = Node(9)
    ans = Solution()
    print(ans.maxDepth(Tree))
