# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            incoming[course] += 1

        dq = deque()
        for index, count in enumerate(incoming):
            if count == 0:
                dq.append(index)

        result = []
        while dq:
            course = dq.popleft()
            result.append(course)

            for next_course in graph[course]:
                incoming[next_course] -= 1
                if incoming[next_course] == 0:
                    dq.append(next_course)

        return result if len(result) == numCourses else []
