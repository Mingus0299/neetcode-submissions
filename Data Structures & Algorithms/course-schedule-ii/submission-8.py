class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_mp  = {i:[] for i in range(numCourses)}
        completed = set()
        visit = set()
        res = []
        for course, prereq in prerequisites:
            prereq_mp[course].append(prereq)

        def dfs(course):
            if course in visit:
                return False
            
            if course in completed:
                return True

            if prereq_mp[course] == []:
                res.append(course)
                completed.add(course)
                return True

            visit.add(course)

            for prereq in prereq_mp[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            prereq_mp[course] = []
            res.append(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
