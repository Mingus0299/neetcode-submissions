class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

# sliding window 
# O(n), O(1)
        answer = curr = 0

        for i in range(k):
            if (blocks[i] == 'W'):
                curr+=1

        i = 0
        answer = curr

        for j in range (k, len(blocks)):
            if (blocks[j] == 'W'):
                curr+=1

            if (blocks[i] == 'W'):
                curr-=1
            i+=1

            answer = min(answer, curr)

        return answer
