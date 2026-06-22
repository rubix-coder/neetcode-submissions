ALGO = {"A":"A$5@&*%@$#^%4","B":"32GE%G@$#Y%","C":"32r8y28y30`2"}

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for c in s:
                encoded += ALGO["A"]+c+ALGO["B"]+ALGO["C"]
            encoded+="SPLIT"
        return encoded


    def decode(self, s: str) -> List[str]:
        
        decoded = ""
        decoded = s.replace(ALGO["A"],"")
        decoded = decoded.replace(ALGO["B"],"")
        decoded = decoded.replace(ALGO["C"],"")

        return (decoded.split("SPLIT")[:-1])
