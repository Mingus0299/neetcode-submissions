class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        def dfs(i, curr):
            if i == len(s):
                res.append(curr.strip())
                return

            for word in wordDict:
                len_w = len(word)
                if i + len_w <= len(s) and s[i: i + len_w] == word:
                    dfs(i+len_w, curr + " " + word)

            
        dfs(0, "")
        return res