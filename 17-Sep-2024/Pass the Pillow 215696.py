# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = 1
        direction = 1  # right: 1  left: 0
        while time:
            # motion
            pos = pos + 1 if direction == 1 else pos - 1
            # direction
            if pos == 1 or pos == n:
                direction ^= 1
            # Time is ticking away
            time -= 1
        return pos
