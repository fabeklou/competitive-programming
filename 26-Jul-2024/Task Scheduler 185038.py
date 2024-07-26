# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks that are ready to be processed 
        available_tasks = [-t for t in Counter(tasks).values()]
        heapify(available_tasks)

        # tasks that can not be processed for now
        pending_tasks = deque()  # (remaining, available_at)
        time = 0

        while available_tasks or pending_tasks:
            if pending_tasks and pending_tasks[0][1] == time:
                new_available_task = pending_tasks.popleft()[0]
                heappush(available_tasks, new_available_task)
            if available_tasks:
                task_to_process = heappop(available_tasks) + 1
                if task_to_process < 0:
                    pending_tasks.append((task_to_process, time + n + 1))
            time += 1

        return time
