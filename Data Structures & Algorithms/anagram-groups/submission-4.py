class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            ls = [0] * 26
            for i in range(len(s)):
                ls[ord(s[i]) - ord('a')]+=1

            res[tuple(ls)].append(s)

        return list(res.values())