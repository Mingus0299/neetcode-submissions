class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtracking(s_i, curr):
            if s_i == len(s):
                res.append(curr.strip())
                return

            for word in wordDict:
                if s_i + len(word) <= len(s) and s[s_i:s_i + len(word)] == word:
                    backtracking(
                        s_i + len(word),
                        curr + " " + word
                    )

        backtracking(0, "")
        return res