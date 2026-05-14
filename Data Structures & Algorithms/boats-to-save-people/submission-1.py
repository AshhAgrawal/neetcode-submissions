class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        boats = 0
        people.sort()
        while l<=r:
            remaining = limit - people[r]
            r-=1
            boats += 1
            if l<=r and remaining >= people[l]:
                l+=1
        return boats

