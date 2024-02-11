class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        stats = {}
        no_loss = []
        one_loss = []

        for winner, loser in matches:
            if winner not in stats:
                stats[winner] = 0

            if loser not in stats:
                stats[loser] = 1
            else:
                stats[loser] += 1

        for player, losses in stats.items():
            if losses == 0:
                no_loss.append(player)
            if losses == 1:
                one_loss.append(player)

        return [ sorted(no_loss), sorted(one_loss) ]