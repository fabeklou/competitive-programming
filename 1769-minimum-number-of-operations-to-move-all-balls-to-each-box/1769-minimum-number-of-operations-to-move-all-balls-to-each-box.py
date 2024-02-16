class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []

        for index1 in range(len(boxes)):
            moves = 0
            for index2 in range(len(boxes)):
                if index1 != index2 and boxes[index2] == '1':
                    moves += abs(index1 - index2)
            result.append(moves)

        return result
