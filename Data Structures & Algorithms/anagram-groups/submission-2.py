class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))

            hashmap[sortedS].append(s)

        return list(hashmap.values())