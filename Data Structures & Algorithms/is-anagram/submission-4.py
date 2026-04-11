class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        s = list(s)
        t = list(t)

        letter_map_s = {}
        letter_map_t = {}

        for letter in s:
            letter_map_s[letter] = letter_map_s.get(letter, 0) + 1

        for letter in t:
            letter_map_t[letter] = letter_map_t.get(letter, 0) + 1

        for opt in letter_map_s:
            if(letter_map_s.get(opt, None) != letter_map_t.get(opt, 200)):
                return False
        return True
            