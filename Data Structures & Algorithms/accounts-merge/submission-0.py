class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        size = {}
        email_to_name = {}

        def find(email):
            if parents[email] != email:
                parents[email] = find(parents[email])
            return parents[email]
        
        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)

            if root1 == root2:
                return 

            if size[root1] < size[root2]:
                parents[root1] = root2
                size[root2] += size[root1]
            else:
                parents[root2] = root1
                size[root1] += size[root2]
        
        for account in accounts:
            name = account[0]
            firstEmail = account[1]

            for email in account[1:]:
                if email not in parents:
                    parents[email] = email
                    size[email] = 1

                email_to_name[email] = name
                union(firstEmail, email)
        group = defaultdict(list)

        for email in parents:
            root = find(email)
            group[root].append(email)

        res = []

        for root in group:

            sortedEmails = sorted(group[root])
            name  = email_to_name[root]
            
            res.append([name] + sortedEmails)
        return res