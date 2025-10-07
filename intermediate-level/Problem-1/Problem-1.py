def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
A= "Machine learning is fascinating"
print(longest_word(A))