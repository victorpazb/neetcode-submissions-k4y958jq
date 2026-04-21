class Solution:
    #author: @victor.braga / criado por mim e comentado por LLM
    def _normalize_string(self, s: str) -> str:
        """
        Normalize a string for palindrome checking.

        Steps performed:
        1. Remove all non-alphanumeric characters (keep only letters and numbers).
        2. Trim leading and trailing whitespace.
        3. Convert all characters to lowercase.
        4. Remove any remaining internal spaces.

        This ensures the string is in a standardized format before comparison.

        Example:
            Input:  "A man, a plan, a canal: Panama"
            Output: "amanaplanacanalpanama"
        """
        # Keep only alphanumeric characters (removes symbols like !, @, spaces, etc.)
        clean_special_char = ''.join(c for c in s if c.isalnum())
        
        # Normalize:
        # - strip(): remove leading/trailing spaces
        # - lower(): make case-insensitive
        # - replace(" ", ""): remove any remaining spaces (extra safety)
        normalized_string = clean_special_char.strip().lower().replace(" ", "")
        
        return normalized_string

    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a palindrome.

        A palindrome reads the same forward and backward.
        This function first normalizes the string (removing non-alphanumeric
        characters and ignoring case), then compares characters from both ends.

        Approach:
        - Use two pointers:
            head -> starts at the beginning
            tail -> starts at the end
        - Compare characters moving inward
        - Stop early if any mismatch is found

        Time Complexity: O(n)
        Space Complexity: O(n) (due to normalized string)

        Example:
            Input:  "A man, a plan, a canal: Panama"
            Output: True
        """
        
        # Normalize input string to ignore case and special characters
        normalized_string = self._normalize_string(s)
        
        # Number of comparisons needed (only half of the string)
        rounds = int(len(normalized_string) / 2)
        
        # Pointers for start (head) and end (tail)
        head = 0
        tail = -1
        
        # Assume it's a palindrome until proven otherwise
        is_palindrome = True
        
        # Compare characters from both ends moving toward the center
        while rounds > 0:
            
            # If mismatch is found, it's not a palindrome
            if normalized_string[head] != normalized_string[tail]:
                is_palindrome = False
                break
            
            # Move pointers inward
            rounds -= 1
            head += 1
            tail -= 1   
        
        return is_palindrome