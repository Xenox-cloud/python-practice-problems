from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
A=["bat", "tab", "cat", "act"]
print(group_anagrams(A))