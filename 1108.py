import re
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = re.findall(r'\d+',address)
        return (f"{result[0]}[.]{result[1]}[.]{result[2]}[.]{result[3]}")
        
