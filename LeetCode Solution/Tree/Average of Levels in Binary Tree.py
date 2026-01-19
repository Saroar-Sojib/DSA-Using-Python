# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        ans = []
        temp_list = []
        temp_list.append(root)
        while temp_list:
            len_temp_list = len(temp_list)
            res = 0
            for i in range(len_temp_list):
                node = temp_list.pop(0)
                res+=node.val
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            ans.append(res/len_temp_list)
        return ans
            
            

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
    print(ans.averageOfLevels(Tree))