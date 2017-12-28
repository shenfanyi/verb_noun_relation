#!/usr/bin/env python2
#-*- coding: UTF-8 -*-


import pandas as pd

def handle_verb(word):
    i = word[3:-1]
    return i

def handle_noun(word):
    i = word[3:-2]
    return i
    
    
lib_raw = pd.read_csv('lib.csv', header = None)
#print lib_raw.iloc[:,0]
lib_raw = lib_raw.drop_duplicates()
lib_raw.iloc[:,0] = lib_raw[0].apply(handle_verb)
lib_raw.iloc[:,1] = lib_raw[1].apply(handle_noun)
lib_raw.columns = ['verb', 'noun']   


verb_unique = lib_raw.iloc[:,0].unique()

dic_final = dict()
            
for verb in verb_unique:
    dic_final[verb] = []
    
for index in lib_raw.index:
    dic_final[lib_raw.loc[index,'verb']].append(lib_raw.loc[index,'noun'])


dic_final = pd.DataFrame([dic_final.keys(),dic_final.values()]).T
#print dic_final

dic_final.to_csv('lib_final.csv',index = False)

    
#data = pd.read_csv('lib_final.csv')
#print data
