import string
import nltk
nltk.download('punkt')

text = open('Building_Global_Community.txt').read()
text = text.lower();

from nltk import word_tokenize
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

texts = word_tokenize(text)
filtered = [ a for a in texts if a.isalnum() ]
filtered = [ a for a in filtered if a not in stopwords]


from collections import Counter
result = Counter(filtered)
print( result )
