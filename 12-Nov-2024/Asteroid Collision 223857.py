# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            if not stk or ast > 0 or stk[-1] < 0:
                stk.append(ast)
            else:
                while stk:
                    if stk[-1] < 0:
                        stk.append(ast)
                        break
                    elif stk[-1] == abs(ast):
                        stk.pop()
                        break
                    elif stk[-1] < abs(ast):
                        stk.pop()
                        if not stk:
                            stk.append(ast)
                            break
                    else:
                        break
        return stk
