class Solution:
    """
    LINHA DE PENSAMENTO:
    
    Essa versão pensei absolutamente sozinho só com caneta e papel
    
    A intenção aqui foi a de pegar duas fraçoes de arrays, que fossem exatamente a exclusão do elemento atual
    
    Ao termos os produtos de parte 1 e parte 2, fazemos o produto de delas e temos o valor esperado para adcionar
    no array de saída
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = []
        i = 1

        while(len(output_array) < len(nums)):
        
            j = i - 1
            output = 1

            for num in nums[:j]:
                output *= num 

            output2 = 1
            for num in nums[i:]:
                output2 *= num 


            output_array.append(output2*output)
            i += 1
            
        return output_array
                