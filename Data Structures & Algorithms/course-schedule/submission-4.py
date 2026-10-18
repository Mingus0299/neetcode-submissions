class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        mp = {i:[] for i in range(numCourses)}

        for crs, pres in prerequisites:
            mp[crs].append(pres)

        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if mp[course] == []:
                return True

            visit.add(course)

            for pre in mp[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            mp[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
