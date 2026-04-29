class TimeMap:

    def __init__(self):
        # Dictionary to store:
        # key → list of [value, timestamp]
        # WHY list? → we store all versions of value over time
        self.store = {} 


    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key not present, initialize empty list
        # WHY? → first time seeing this key
        if key not in self.store:
            self.store[key] = []

        # Append value and timestamp
        # WHY append? → timestamps are strictly increasing → list stays sorted
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # Default result if no valid timestamp found
        res = ""

        # Get list of [value, timestamp] for the key
        # If key doesn't exist → return empty list
        values = self.store.get(key, [])

        # Binary search to find the closest timestamp ≤ given timestamp
        # WHY binary search? → list is sorted by timestamp
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # If current timestamp is valid (≤ target)
            if values[m][1] <= timestamp:
                # Update result to this value
                # WHY? → this could be the best candidate so far
                res = values[m][0]

                # Move right to find a closer timestamp
                # WHY? → we want the largest timestamp ≤ given timestamp
                l = m + 1
            else:
                # If timestamp too large, move left
                r = m - 1

        # Return best found value (or "" if none)
        return res