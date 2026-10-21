class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        prereq_mp = {i:[] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            prereq_mp[crs].append(prereq)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False

            if prereq_mp[crs] == []:
                return True

            visiting.add(crs)

            for pre in prereq_mp[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            prereq_mp[crs] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

            