#!/usr/bin/env python2
#-*- coding: UTF-8 -*-

import pandas as pd
import sys


vvn_pd = pd.read_csv('verb_verbs_nouns.csv', index_col = 'verb')
#print vvn_pd.loc['foul','nouns']


input_verb = sys.argv[1]

try:
    output = vvn_pd.loc[input_verb,'nouns'] + '1'
except KeyError:
    output = 0
    for i,j in zip(vvn_pd.verbs,vvn_pd.nouns):
        #print i,j
        if input_verb in i:
            output = j + '2'
    if output == 0:
        output = 'verb is not included'
          
          
print output
