class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out ={}
        for x in nums:
            if x in out:
                out[x]+=1
            else:
                out[x]=1
        temp_key = sorted(out, key=out.get, reverse=True)
        # temp_key.sort()
        return temp_key[:k]