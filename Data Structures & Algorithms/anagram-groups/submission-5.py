class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for s in strs:
            lst = [0] * 26
            for c in s:
                lst[ord(c)-ord('a')]+=1

            mp[tuple(lst)].append(s)

        
        return list(mp.values())

            
        