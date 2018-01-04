#!/usr/bin/env python2
#-*- coding: UTF-8 -*-


import pandas as pd
from gensim.models.word2vec import Word2Vec

data_pd = pd.read_csv('lib_final.csv')

def lower_str(stri):
    return stri.lower()

def handle_str(stri):
    res = []
    cutted = stri[1:-1].replace("'","").split(',')
    for i in cutted:
        j = i.lower().strip()
        res.append(j)
    return res

print handle_str(data_pd.iloc[-1,1][1:-1])

data_pd.iloc[:,1] = data_pd.iloc[:,1].apply(handle_str)
data_pd.iloc[:,0] = data_pd.iloc[:,0].apply(lower_str) 
#print data_pd

all_verbs_pd = pd.DataFrame(range(len(data_pd.iloc[:,0])), index = data_pd.iloc[:,0])
all_verbs_dic = dict(zip(all_verbs_pd.index, all_verbs_pd.iloc[:,0]))
#print all_verbs_pd
#print all_verbs_dic
#print all_verbs_dic.values

cons_verbs_dic = {}
cutted_verbs_dic = {}
added_verbs_dic = {}

for (word,index) in all_verbs_dic.items():
    #print word[-3:] == 'ing',index
    #break
    if word[-3:] == 'ing':
        cutted_verb = word[:-3]
        cutted_verbs_dic[cutted_verb] = index
        added_verb = cutted_verb+'e'
        added_verbs_dic[added_verb] = index
    elif word[-2:] == 'ed':
        cutted_verb = word[:-2]
        cutted_verbs_dic[cutted_verb] = index
        added_verb = cutted_verb+'e'
        added_verbs_dic[added_verb] = index
    elif word[-1:] == 's':
        cutted_verb = word[:-1]
        cutted_verbs_dic[cutted_verb] = index
        if cutted_verb[-1:] == 'e':
            added_verb = cutted_verb[-1:]
            added_verbs_dic[added_verb] = index
        cons_verbs_dic[word] = index
    else:
        cons_verbs_dic[word] = index
        
#print len(cons_verbs_dic)
#print len(cutted_verbs_dic)
#print len(added_verbs_dic)


lists = list()
list_index = list()
for i in all_verbs_dic:
    if i not in list_index:
        li = list()
        li.append(all_verbs_dic[i])
        for j in cutted_verbs_dic:
            if i == j:
                li.append(cutted_verbs_dic[j])
                list_index.append(cutted_verbs_dic[j])
                lists.append(li)
        for m in added_verbs_dic:
            if i == m:
                li.append(added_verbs_dic[m])
                list_index.append(added_verbs_dic[m])
                lists.append(li)
print len(lists)
#print list_index

lists_drop_dup = []
for i in lists:
    if i not in lists_drop_dup:
        lists_drop_dup.append(i)
print len(lists_drop_dup)

def remove_stops(li):
    res = []
    stop_words = ['@','who', 'what', 'how', 'why', 'where', 'when']
    for i in li:
        if i not in stop_words:
            res.append(i)
    return res


rows = []
for i in lists_drop_dup:
    row1 = []
    row2 = []
    row = [row1,row2]
    for j in i:
        row1.append(data_pd.iloc[j,0])
        row2.extend(data_pd.iloc[j,1])
    rows.append(row)
    #print row

nv_pd = pd.DataFrame(rows)
nv_pd.iloc[:,1] = nv_pd.iloc[:,1].apply(remove_stops)
print nv_pd
