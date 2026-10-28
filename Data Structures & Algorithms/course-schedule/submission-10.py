class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mp_prereq = {i : [] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            mp_prereq[crs].append(prereq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            
            if mp_prereq[course] == []:
                return True

            visit.add(course)
            for prereq in mp_prereq[course]:

                if not dfs(prereq):
                    return False
            visit.remove(course)
            mp_prereq[course] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True

        