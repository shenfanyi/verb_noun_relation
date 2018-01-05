#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
 
 
import sys
import glob
import errno

import plac
import spacy
from spacy.symbols import nsubj, VERB, NOUN


#file = open('w_au_b.txt', 'r') 
#j = 0
#raw = list()
#for i in file:
    #raw.append(i)

raw = list()
path = 'corpus/*.txt'   
files = glob.glob(path)
#print files
for name in files: 
    try:
        with open(name) as f: 
            for i in f:
                raw.append(i)
    except IOError as exc:
        if exc.errno != errno.EISDIR: 
            raise 


nlp = spacy.load('en')


def chunks(docu):
    lists = list() 
    for i in range(0, len(docu), 2):
        ls = docu[i:(i + 2)]
        lists.append(ls)
    return lists

raw_splitted = list()
for i in raw:
    p = i.split('.')
    raw_splitted.extend(p)
#print raw_splitted

libs = list()
        
for i in raw_splitted:
    #print type(i)
    i = unicode(i, 'unicode-escape')
    doc = nlp(i)

    for possible_subject in doc:
        lib = list()
        if possible_subject.pos == NOUN and possible_subject.head.pos == VERB:
            lib.append(possible_subject.head.text)
            lib.append(possible_subject.text)
            if len(lib) != 0:
                li = chunks(lib)
                #print li
                libs.extend(li)
                
#print len(libs)
#print libs[-20:]


with open('lib.txt', 'w') as file:
    for i in libs:
        file.writelines("%s\n" % i)
        
        






    
