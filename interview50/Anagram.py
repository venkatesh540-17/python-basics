from collections import Counter


def anagram(s1,s2):
    return sorted(s1)==sorted(s2)
print(anagram("rat","tar"))

def anagram2(s1,s2):

    return Counter(s1) == Counter(s2)
print(anagram2("cat","tac"))