# Homework2

### Examples of Markdownn from http://www.markdowntutorial.com/

- [x] Homework Uploaded

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/6A5EpqqDOdk/0.jpg)](https://www.youtube.com/watch?v=6A5EpqqDOdk)

#### Code sample: 
```python
file = open('Building_Global_Community.txt')
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

from collections import defaultdict, Counter
 PosWordsCount = defaultdict(Counter)

for line in file:
    Twords = word_tokenize(line)
    Pwords = nltk.pos_tag(Twords)
    for word, pos in Pwords:
        PosWordsCount[pos][word] += 1
        
for pos, counter in  PosWordsCount.items():
    print(pos, ':', end=' ')
    for word, count in counter.most_common(5):
        print(word, '/', count, end=' ')
    print()

```

