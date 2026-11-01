class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_list = [[] for i in range(numCourses)]

        for prereq, course in prerequisites:
            adj_list[course].append(prereq)
        
        mp = {}

        def dfs(course):
            if course not in mp:
                mp[course] = set()
                for prereq in adj_list[course]:
                    mp[course] |= dfs(prereq)
                mp[course].add(course)

            return mp[course]

        for i in range(numCourses):
            dfs(i)

        res = []

        for pre, course in queries:
            res.append( pre in mp[course])
        return res
            