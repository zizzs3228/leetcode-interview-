class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a = 0
        for i in range(len(operations)):
            if operations[i]=="--X" or operations[i]=="X--":
                a-=1
            if operations[i]=="++X" or operations[i]=="X++":
                a+=1
