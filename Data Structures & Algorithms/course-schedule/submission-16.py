class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq_list = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_list[course].append(prereq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
                
            if prereq_list[course] == []:
                return True

            visit.add(course)

            for prereq in prereq_list[course]:
                if not dfs(prereq):
                    return False

            prereq_list[course] = []
            visit.remove(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        