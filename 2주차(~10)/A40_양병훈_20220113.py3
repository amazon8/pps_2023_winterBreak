class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel =  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        l = len(s)//2
        a = s[:l]
        b = s[l:]
        return len([i for i in a if i in vowel])==len([i for i in b if i in vowel])