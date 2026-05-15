class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []

        for i in range(len(ops)):
            if ops[i] == "C":
                record.pop()
            elif ops[i] == "D":
                val = 2 * record[-1]
                record.append(val)
            elif ops[i] == "+":
                val = record[-1] + record [-2]
                record.append(val)    
            else:
                record.append(int(ops[i]))
        return sum(record)