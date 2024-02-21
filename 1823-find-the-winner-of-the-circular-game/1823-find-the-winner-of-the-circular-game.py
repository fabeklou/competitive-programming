class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # If we only have one player, he automatically wins
        # And if <k> is <1> the winner is the last player
        if k == 1:
            return n

        players = [p for p in range(1, n + 1)]
        # This can be seen as the last element/player deleted
        # While k is the distance between this element
        #   and the next element to delete
        del_index = 0

        while True:
            # Get index of the element to delete
            #   (-1) because the size of our list is smaller by one
            #   at each iteration and the next element takes the
            #   index of the deleted element
            del_index = del_index + k - 1

            # Avoid List Index Out of Range error
            del_index %= len(players)

            # Delete the choosen payer
            del players[del_index]

            # The winner is the only player remaining
            if len(players) == 1:
                winner = players[0]
                break

        return winner
                