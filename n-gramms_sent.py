from nltk.util import bigrams, trigrams, ngrams
from nltk.corpus import inaugural
from nltk import FreqDist

speech_wash = list(inaugural.sents('1789-Washington.txt'))
speech_adams = list(inaugural.sents('1797-Adams.txt'))
speech_lincoln = list(inaugural.sents('1861-Lincoln.txt'))

wash = []
for i in speech_wash:
    wash_b = list(bigrams(i, pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>'))
    wash.extend(wash_b)

adams = []
for a in speech_adams:
    adams_b = list(bigrams(a, pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>'))
    adams.extend(adams_b)

lincoln = []
for l in speech_lincoln:
    lincoln_b = list(bigrams(l, pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>'))
    lincoln.extend(lincoln_b)

wash_freq = FreqDist()
lincoln_freq = FreqDist()
adams_freq = FreqDist()
lincoln_fd = FreqDist(lincoln)

wash_freq = FreqDist(wash)
print("washington freq", wash_freq.most_common())

adams_freq = FreqDist(adams)
print("Adams freq", adams_freq.most_common(10))

lincoln_freq = FreqDist(lincoln)
print("Lincoln freq", lincoln_freq.most_common(10))