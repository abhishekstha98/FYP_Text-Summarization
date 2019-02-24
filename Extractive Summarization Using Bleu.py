import wikipedia
import nltk
from nltk.translate.bleu_score import sentence_bleu
import re
import math

name = input("please enter a name : ")
#name = 'Albert Einstein'

#following are the list of words that are useless for summarization
pro_nouns = ['i','is', 'you', 'he', 'she', 'it','its' 'which', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'what', 'who', 'whom', 'mine', 'yours', 'his', 'hers', 'ours', 'theirs', 'this', 'that', 'these', 'those', 'which', 'whose', 'whoever', 'whatever', 'whichever', 'whomever', 'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'themselves']
adverb = ['and', 'or', 'but', 'nor', 'so', 'for', 'yet', 'after', 'although', 'as', 'as if', 'as long as', 'because', 'before', 'even if', 'even though', 'once', 'since', 'so that', 'though', 'till', 'unless', 'until', 'what', 'when', 'whenever', 'wherever', 'whether', 'while']
prepositions = ['about', 'above', 'across', 'after', 'against','on', 'by', 'among', 'around', 'at', 'before', 'behind', 'below', 'beside', 'between', 'by', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'near', 'of', 'off', 'on', 'out', 'over', 'through to', 'toward', 'under', 'up', 'with']
article = ['a', 'an', 'the']


txttosummarize = wikipedia.page(name)
b4clean = txttosummarize.content
y = txttosummarize.content

y = y.lower()
#y = y.split('. ') # y is the list of sentences
y = re.split('(?<=[.\n]) +',y)
z = []
l = len(y)
for loop in range (0,l-1):
    new = y[loop].split(' ')
    z.append(new) #new list to make list of lists of words of different sentences
candidate = z
l = len(z)
for loop in range (0,l-1): # loop for removing duplicate words
    z[loop] = list(dict.fromkeys(z[loop]))

new_list = []
new_list1 = []
new_list2 = []
new_list3 = []

#removing article
for loop in range(0,len(z)-1):
    temp = []
    for x in z[loop]:
        if x not in article:
            temp.append(x)
    new_list.append(temp)

#removing prepositions
for loop in range(0,len(z)-1):
    temp = []
    for x in new_list[loop]:
        if x not in prepositions:
            temp.append(x)
    new_list1.append(temp)


#removing pronouns
for loop in range(0,len(z)-1):
    temp = []
    for x in new_list1[loop]:
        if x not in pro_nouns:
            temp.append(x)
    new_list2.append(temp)

#removing adverb
for loop in range(0,len(z)-1):
    temp = []
    for x in new_list2[loop]:
        if x not in adverb:
            temp.append(x)
    new_list3.append(temp)



    
#print(new_list3[:4])
s_score = [] # list to store the scores for sentences
sorted_s = []
line_no = int(input("enter the number of lines that you want to summarize(>2): "))
for loop in range(0,line_no):
    score = sentence_bleu(new_list[:300], candidate[loop], weights=(5, 1, 0, 1)) #scoring mechanism
    s_score.append(score)


    
sline_no = math.floor(line_no/3) # summarized output will be the 1/3 size of the paragraph
asd = sorted( [(x,i) for (i,x) in enumerate(s_score)], reverse=True )[:sline_no]
for loop in range(0,sline_no):
    sorted_s.append(asd[loop][1])
sorted_s.sort()
for loop in range(0,sline_no):
    print(str(loop + 1)+'.  ' + ' '.join(candidate[sorted_s[loop]])) # displaying the sentences with highest score according to the position in the paragraphs

    
































