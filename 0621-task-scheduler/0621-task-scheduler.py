class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1

        freq = sorted(count.values(), reverse=True)

        max_freq = freq[0]

        max_count = 0
        for f in freq:
            if f == max_freq:
                max_count += 1

        time = (max_freq - 1) * (n + 1) + max_count
        return max(time, len(tasks))