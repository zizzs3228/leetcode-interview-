class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for drag in jewels:
            count+=stones.count(drag)
        return count
