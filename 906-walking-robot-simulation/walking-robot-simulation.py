class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        mp = defaultdict(set)
        for k,v in obstacles:
            mp[k].add(v)
        dirs = ["East", "North", "West", "South"] 
        vals = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        cur = 1
        pos = [0, 0]
        ans = 0
        for cmd in commands:
            if cmd == -1:
                cur = (cur + 3) % 4
            elif cmd == -2:
                cur = (cur + 1) % 4
            else:
                x, y = pos
                delx, dely = vals[cur]
                for step in range(1, cmd+1):
                    new_x, new_y = x + step * delx , y + step * dely
                    if new_y not in mp[new_x]:
                        ans = max(ans, new_x * new_x + new_y * new_y)
                        pos = [new_x, new_y]
                    else:
                        break
            # print(pos, ans, cur)
        return ans