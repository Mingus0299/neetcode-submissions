class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs:
            ls = [0] * 26

            for c in s:
                ls[ord(c) - ord('a')]+=1

            mp[tuple(ls)].append(s)


        return list(mp.values())

