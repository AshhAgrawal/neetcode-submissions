class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for a, b in trust:
            incoming[a] += 1
            outgoing[b] += 1
        for i in range(1, n+1):
            if incoming[i] == 0 and outgoing[i] == n-1:
                return i
        return -1