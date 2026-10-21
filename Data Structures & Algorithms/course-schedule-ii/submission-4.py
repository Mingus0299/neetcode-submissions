class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq_mp = {i : [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            prereq_mp[crs].append(prereq)
        
        completed = set()
        visiting = set()
        output = []

        def dfs(crs):
            if crs in visiting:
                return False

            if crs in completed:
                return True
            
            
            visiting.add(crs)
            for pre in prereq_mp[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            completed.add(crs)
            output.append(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return[]

        return output
                