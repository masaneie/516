from nltk.book import *
print([w for w in text6 if w.endswith('ise')]) 
# for this code I wrote print the words that are in text 6 if they end with 'ise' , I used w.edswith as we had in our table 4.2 
# in chapter 1
print([term for term in text6 if 'z' in term])
# for this code I wrote terms in text6 if they contain (z)
print([term for term in text6 if 'pt' in term])
# this code was like the pervious one expect that I have to include a sequence of letters (pt) instead of (z)
print([item for item in text6 if item.istitle()])
# for this code I used item.istitle () because if items contain cased characters and are titlecased, they will be included then 
# for this code I was inspited by the code that we had under table 4.2 in chapter 1

List1=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print([w for w in List1 if w.endswith('sh')])
print([w for w in List1 if len(w)>4])
# for these codes, first I created List 1, then for the first code I wrote print the words in List 1 if they sratwith (sh). W.endwith
#was again part of the code that we ha in table 4.2. For the other code also I wrote print the words that are longer that 4 letters. len 
# is part of the code here that has been explained in chapter 1. It refers to the length. 
