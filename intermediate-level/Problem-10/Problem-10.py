import re
from collections import Cou

def most_frequent_word(text, stopwords):
    words = re.findall(r'\w+', text.lower())
    filtered = [w for w in words if w not in stopwords]
    counter = Counter(filtered)
    return counter.most_common(1)[0]

stopwords = {"the", "is", "and", "in", "to", "of"}
text = "Machine learning is the future and machine learning is powerful"
print(most_frequent_word(text, stopwords))