class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        map_s = {}
        map_t = {}

        for letter in s:
            map_s[letter] = map_s.get(letter, 0) + 1

        for letter in t:
            map_t[letter] = map_t.get(letter, 0) + 1

        return map_s == map_t
                