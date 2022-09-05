class Solution:
    def matrixReshape(self, mat, r, c):
        res = []
        for x in mat:
            res+=x
        final_res = []
        if len(res)%c==0:
            if len(res)//c==r:
                temp_res = []
                for i in range(0,len(res)):
                    if (i+1)%c==0:
                        temp_res.append(res[i])
                        final_res.append(temp_res)
                        temp_res = []
                    else:
                        temp_res.append(res[i])
                return final_res
            else:
                return mat
        else:
            return mat             
ans = Solution()
print(ans.matrixReshape([[1,2],[3,4]],4,1))