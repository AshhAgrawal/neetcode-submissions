class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        q = deque(["0000"])
        visited.add("0000")
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        newLock = lock[:i] + digit + lock[i+1:]
                        if newLock in visited:
                            continue
                        if newLock == target:
                            return steps
                        q.append(newLock)
                        visited.add(newLock)
        return -1