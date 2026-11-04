class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visit = set()
        visit.update(deadends)
        visit.add("0000")

        def children(lock):
            res = []
            for i in range(4):
                up = str((int(lock[i])+1) % 10)
                down = str((int(lock[i])-1+10) % 10)
                res.append(lock[:i] + up + lock[i+1:])
                res.append(lock[:i] + down + lock[i+1:])
            return res

        q = deque()
        q.append(["0000", 0])
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    q.append([child, turns+1])
                    visit.add(child)
        
        
        return -1


