class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj_list = {i : [] for i in range(numCourses)}

        for prereq, course in prerequisites:
            adj_list[course].append(prereq)

        total_prereq = {}

        def dfs(course):
            if course in total_prereq:
                return total_prereq[course]

            total_prereq[course] = set()

            for prereq in adj_list[course]:
                total_prereq[course] |= dfs(prereq)
            total_prereq[course].add(course)

            return total_prereq[course]

        for i in range(numCourses):
            dfs(i)

        res = []

        for prereq, course in queries:
            res.append(prereq in total_prereq[course])
        return res
        