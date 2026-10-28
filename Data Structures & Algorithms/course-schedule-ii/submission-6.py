class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_mp = {i : [] for i in range(numCourses)}\

        for course, prereq in prerequisites:
            prereq_mp[course].append(prereq)

        res = []
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            
            if prereq_mp[course] == []:
                if course not in res:
                    res.append(course)
                return True

            visit.add(course)
            for prereq in prereq_mp[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            prereq_mp[course] = []
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


            