class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            'FizzBuzz' if item % 15 == 0
            else 'Fizz' if item % 3 == 0
            else 'Buzz' if item % 5 == 0
            else str(item)
            for item in range(1, n + 1)
        ]
