class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        while len(nums1)!=m:
            nums1.pop()
        while len(nums2)!=n:
            nums2.pop()
        return nums1+nums2

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
print(Solution().merge(nums1,m,nums2,n))