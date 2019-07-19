from nltk.util import bigrams, trigrams, ngrams
from nltk.corpus import inaugural
from nltk import FreqDist

'''random_sentence = "I love turtles."
random_words = ["I", "love", "turtles", "more", "than", "you", "ever", "will", "!"]

#print(list(bigrams(random_text)))
print(list(bigrams(random_words)))
for trg in (ngrams(random_sentence, 4,
                   pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>')):
    print(trg)'''

speech_wash = inaugural.words('1789-Washington.txt')
speech_adams = inaugural.words('1797-Adams.txt')
speech_lincoln = inaugural.words('1861-Lincoln.txt')

wash = bigrams(speech_wash, pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>')
adams = bigrams(speech_adams, pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>')
lincoln = bigrams(speech_lincoln, pad_right=True, right_pad_symbol='</s>',
                   pad_left=True, left_pad_symbol='<s>')

collection = []
collection.append(list(wash))
collection.append(list(adams))
collection.append(list(lincoln))

wash_freq = FreqDist()
lincoln_freq = FreqDist()
adams_freq = FreqDist()

wash_freq = FreqDist(collection[0])
print("washington freq", wash_freq.most_common())

adams_freq = FreqDist(collection[1])
print("Adams freq", adams_freq.most_common(10))

lincoln_freq = FreqDist(collection[2])
print("Lincoln freq", lincoln_freq.most_common(10))






