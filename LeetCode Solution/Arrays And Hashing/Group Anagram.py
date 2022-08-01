class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for s in strs:
            sorted_value = ''.join(sorted(s))
            if sorted_value in out:
                out[sorted_value].append(s)
            else:
                out[sorted_value]=[s]
        return out.values()