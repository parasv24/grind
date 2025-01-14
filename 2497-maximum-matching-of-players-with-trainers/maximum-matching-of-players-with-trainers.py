class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        ans = 0
        while i < len(players) and j < len(trainers):
            if trainers[j]>= players[i]:
                i += 1
                j += 1
                ans += 1
            else:
                j+=1
        return ans
        