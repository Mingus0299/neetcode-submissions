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

        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in mp[v])
        return res