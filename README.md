# verb_noun_relation

1,Project:

research of relation between verb and noun from specific corpus


2,Aim:

build a verb-noun database


3,Source of data:

Wikipedia corpus(170,000 sentences)

link: https://www.corpusdata.org/intro.asp


4,Content:

cutting articles

words segmentation

POS Tagging

Dependency Parse

Named Entities

Tokenization

Rule-based Matching


5, Process and Result

eg1.

input: python recommend_API.py foul

output: ['something', 'pollutants', 'river']1    

(1: input verb is original type)

eg2.

input: python recommend_API.py fouling

output: ['something', 'pollutants', 'river']2    

(2: input verb is transferred type)

eg3.

input: python recommend_API.py foull

output: verb is not included

