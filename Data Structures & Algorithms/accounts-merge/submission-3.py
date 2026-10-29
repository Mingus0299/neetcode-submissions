class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]

        return cur

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1

        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        emailToAcc = {} #email -> index of account

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])

                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list) # index of acc -> list of emails
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name]+ sorted(emailGroup[i]))

        return res
        