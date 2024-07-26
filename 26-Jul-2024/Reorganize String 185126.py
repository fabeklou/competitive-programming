# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(max_heap)
        waiting = 0  # count, char
        result = []

        while max_heap:
            if max_heap:
                curr_char_count, curr_char = heappop(max_heap)
                result.append(curr_char)
                if waiting:
                    heappush(max_heap, waiting)
                    waiting = 0
                if curr_char_count + 1 < 0:
                    waiting = curr_char_count + 1, curr_char
            if waiting and not max_heap:
                return ''

        return ''.join(result)
