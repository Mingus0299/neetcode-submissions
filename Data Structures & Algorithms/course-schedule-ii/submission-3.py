class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        mp = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            mp[course].append(pre)

        cycle = set()
        completed = set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in completed:
                return True

            cycle.add(course)
            for pre in mp[course]:

                if not dfs(pre):
                    return False
            cycle.remove(course)
            completed.add(course)
            res.append(course)
            
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res

            