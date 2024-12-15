class RoundRobinScheduler:
    def __init__(self):
        self.n = 0
        self.quantum = 0

    def set_parameters(self, n, quantum):
        self.n = n
        self.quantum = quantum

    def calculate(self, arrival_times, burst_times):
        """Thuật toán Round Robin."""
        remaining_time = burst_times[:]
        time = 0
        queue = []
        is_in_queue = [False] * self.n
        gantt_chart = []

        for i in range(self.n):
            if arrival_times[i] <= time:
                queue.append(i)
                is_in_queue[i] = True

        while sum(remaining_time) > 0:
            if not queue:
                time += 1
                continue

            i = queue.pop(0)
            run_time = min(self.quantum, remaining_time[i])
            gantt_chart.append((i, time, time + run_time))
            time += run_time
            remaining_time[i] -= run_time

            for j in range(self.n):
                if arrival_times[j] <= time and not is_in_queue[j]:
                    queue.append(j)
                    is_in_queue[j] = True

            if remaining_time[i] > 0:
                queue.append(i)

        return {"gantt_chart": gantt_chart}
