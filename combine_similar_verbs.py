 #!/usr/bin/env python2
#-*- coding: UTF-8 -*-

import pandas as pd
from gensim.models.word2vec import Word2Vec

data = pd.read_csv('lib_final.csv')
#print data

#model= Word2Vec()
#model.build_vocab_from_freq({"Word1": 15, "Word2": 20})

#model = Word2Vec(list(data), min_count=5)

#model = Word2Vec(iter=1)  # an empty model, no training yet
#model.build_vocab(data)  # can be a non-repeatable, 1-pass generator
#model.train(data)  # can be a non-repeatable, 1-pass generator


#sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
model = Word2Vec(data, min_count=1)
for i in model.wv:
    print i
