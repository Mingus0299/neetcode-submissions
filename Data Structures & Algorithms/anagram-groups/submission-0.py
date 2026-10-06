class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# hash table

        mp = defaultdict(list)

        for word in strs:
            ls = [0] * 26
            for c in word:
                ls[ord(c) - ord('a')] +=1

            mp[tuple(ls)].append(word)


        return list(mp.values())
