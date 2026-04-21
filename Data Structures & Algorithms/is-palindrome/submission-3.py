class Solution:
    """
    Solução proposta pela LLM a fim melhorar o desempenho

    Me parece que a principal ideia da melhoria é trabalhar com a string que já se tem,
    ao invés de criar uma nova.

    
    """
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # pula caracteres não alfanuméricos
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # compara ignorando case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True