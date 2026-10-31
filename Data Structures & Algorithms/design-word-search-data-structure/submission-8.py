class TrieNode():
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True        

    def search(self, word: str) -> bool:
        
        def backtrack(i, cur):
            if i == len(word):
                return cur.endWord

            if word[i] == ".":
                for child_node in cur.children.values():
                    if backtrack(i+1, child_node):
                        return True
                return False

            else:
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
                return backtrack(i+1, cur)

        return backtrack(0, self.root)