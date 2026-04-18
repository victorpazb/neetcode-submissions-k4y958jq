class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for index, num in enumerate(nums):
            if num not in myMap:
                myMap[num] = [index, 1]  # [primeiro index, ocorrência]
            else:
                myMap[num][1] += 1       # incrementa ocorrência

        # Ordena pela ocorrência (x[1][1]) decrescente
        ordenado = sorted(myMap.items(), key=lambda x: x[1][1], reverse=True)

        # Pega os k primeiros e retorna só as chaves (os números)
        return [num for num, _ in ordenado[:k]]

        