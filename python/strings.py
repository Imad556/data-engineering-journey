#PRACTICING STRINGS IN PYTHON
#PROBLEM 1:
#REVERSE A STRING
def reverse_string(s):
    return s[::-1]

#PROBLEM 2:
#CHECK IF A STRING IS A PALINDROME
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1] 



#PROBLEM 3:
s=input().strip()
even_chars=[::2]
odd_chars=[1::2]
print(even_chars)
print(odd_chars)

#PROBLEM 4:
def anagram_check(s1, s2):
    return sorted(s1) == sorted(s2)


#PROBLEM 5:

from collections import Counter
def count_characters(s):
    count= Counter(s)
    return count


#PROBLEM 6:
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])


#PROBLEM 7:
#removing duplicates
def remove_duplicates(s):
    res= "".join(dict.fromkeys(s))
    return res