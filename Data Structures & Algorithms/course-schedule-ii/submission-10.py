class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_list = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_list[course].append(prereq)

        visit = set()
        res = []
        def dfs(course):
            if course in visit:
                return False

            if prereq_list[course] == []:
                if course not in res:
                    res.append(course)
                return True

            visit.add(course)
            for prereq in prereq_list[course]:
                if not dfs(prereq):
                    return False

            visit.remove(course)
            prereq_list[course] = []
            res.append(course)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return res
                

        