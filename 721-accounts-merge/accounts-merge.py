class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        rank = [0] * len(accounts)
        email_mp = {}
        emails = []
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(x, y):
            px, py = find(x), find(y)
            rx, ry = rank[px], rank[py]
            if px == py:
                return False
            if rx < ry:
                rx, ry = ry, rx
                px, py = py, px
            
            parent[py] = px

            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        for i in range(0, len(accounts)):
            name = accounts[i][0]
            for email in accounts[i][1:]:
                if email not in email_mp:
                    email_mp[email] = i
                    emails.append(email)
                else:
                    union(i, email_mp[email])
        emails.sort()
        grouped_emails = defaultdict(list)
        ans = []
        for email in emails:
            p = find(email_mp[email])
            grouped_emails[p].append(email)
        for k ,v in grouped_emails.items():
            v.sort()
        for i in range(len(accounts)):
            if parent[i] == i:
                ans.append([accounts[i][0], *grouped_emails[i]])

        return ans
