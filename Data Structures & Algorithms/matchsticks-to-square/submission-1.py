class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        target = sum(matchsticks) // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False

        def dfs(index):
            if index == len(matchsticks):
                return (
                    sides[0] == target and
                    sides[1] == target and
                    sides[2] == target and
                    sides[3] == target
                )        
            currMatch = matchsticks[index]
            for side in range(4):
                currSum = sides[side] + currMatch
                if currSum > target:
                    continue
                sides[side] += currMatch

                if dfs(index + 1):
                    return True
                sides[side] -= currMatch

                if sides[side] == 0:
                    break
            return False

                    
        return dfs(0)