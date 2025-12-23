class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        n = len(events)

        # suffix_max[i] = max value from events[i:] onward
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        ans = 0

        for i in range(n):
            s, e, v = events[i]
            ans = max(ans, v)  # take only one event

            # Find first event that starts after this one ends
            j = bisect.bisect_right(events, e, key=lambda x: x[0])

            if j < n:
                ans = max(ans, v + suffix_max[j])

        return ans