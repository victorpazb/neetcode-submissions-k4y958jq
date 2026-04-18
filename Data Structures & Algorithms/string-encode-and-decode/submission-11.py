class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"  # "neet" → "4#neet"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)        # acha o próximo #
            length = int(s[i:j])       # lê o tamanho
            result.append(s[j+1:j+1+length])  # pula exatamente `length` chars
            i = j + 1 + length
        return result
        