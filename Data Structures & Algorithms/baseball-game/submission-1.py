class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        res = 0
        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
                res += record[-1]
            elif op == "C":
                res -= record[-1]
                record.pop()
            elif op == "D":
                record.append(2*record[-1])
                res += record[-1]
            else:
                record.append(int(op))
                res += int(op)
        return res