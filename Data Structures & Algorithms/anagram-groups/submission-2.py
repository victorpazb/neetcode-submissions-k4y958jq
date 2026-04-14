class Solution:
    def _normalize(self, word):
        return "".join(sorted(word.lower()))
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output_array = []
        word_map = {}

        for i, word in enumerate(strs):
            key = self._normalize(word)
            word_map.setdefault(key, []).append(i)

        for indexes in word_map.values():
            temp_array = []
            for index in indexes:
                temp_array.append(strs[index])
            
            output_array.append(temp_array)

        return output_array
        

