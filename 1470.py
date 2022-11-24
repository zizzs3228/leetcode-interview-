class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y=nums[n:]
        x=nums[:n]
        ans=[]
        x.reverse()
        y.reverse()
        for i in range(n):
            ans.append(x.pop())
            ans.append(y.pop())
        return ans
