import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    c = Counter()
    with open(harry_text, 'r') as f:
        h = [line.strip() for line in f.readlines()]
    with open(stopwords_file, 'r') as f:
        s = set([line.strip() for line in f.readlines()])
    h = ' '.join(h)
    f = ''
    for char in h:
        if char.isalnum() or char.isspace():
            f += char.lower()
    c = Counter(f.split())
    for word in s:
        del c[word]

    return (c.most_common(1)[0][0], c.most_common(1)[0][1])
    

