"""
Ponto 1:
 Chave desse problema é que so precisamos retornar a maior serie. 

Ponto 2:
 Como precisa ser O(n), precisamos fazer esses retorno com apenas uma passagem pelo array

Ponto 3: 
 Uma das sacadas é entender que a medida que vamos passando pelo array, vamos atualizando, se necessário o, o retorno. 
"""
#CASE: [10, 11, 12, 1, 2]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)                     #......Uma maneira de elinimar os repetidos, que em nada mudam a série
        largest = 0
        for num in num_set:
            if(num - 1 not in num_set):         #.......Significa que num é o primeiro de uma série
                length = 1                      #.......O tamanho mínimo de uma série
                while num + length in num_set:  #.......Enquanto o num (que ja comprovadamente eh o cabeça da série)
                    length += 1                 #.......Vai dando passos de um em um para aumentar a série, assim vai olhar todo o array para dar o tamanho da serie
                largest = max(largest, length)  #.......Uma maneira simples de atualizar o maior entre eles a cada rodada
        return largest

            

            


        