class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_mp = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_mp[course].append(prereq)

        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if prereq_mp[course] == []:
                return True
            
            visiting.add(course)
            for prereq in prereq_mp[course]:
                if not dfs(prereq):
                    return False
            
            prereq_mp[course] = []
            visiting.remove(course)

            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True
