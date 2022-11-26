class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for sentense in sentences:
            if len(sentense.split())>count:
                count=len(sentense.split())
        return count
