import nltk 
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
# for this code I was inspired by a code on genres and models using conditionalFreqDist. A conditional frequency distribution needs to pair each event with a condition.
# here I used cdf to loop over every word in the genre, producing pairs consisting of the genre and the word.
genres = ['news','science_fiction', 'romance']
# we define the list of genres that we want to include 
typic_words = ['policy', 'conflict', 'party','planet', 'love', 'heart', 'tears']
# we define the list of words whose presence (or absence) may be typical of a genre
cfd.tabulate(conditions=genres, samples=typic_words)
# the results show that as we expected words such as 'policy' or 'conflict' were repeated in the newssubsection, while 'love', 'heart', and 'tears' were 
# most common in the romance subsection of Browncorpus.  In addition, a word such as 'planet' was non-existant in news and romantic texts, yet appeared 10 times in 
# science fiction texts.  


	
from nltk.corpus import brown
from nltk.probability import FreqDist
# we need to import FreqDist
bigrams = nltk.bigrams(nltk.corpus.brown.words(categories="news"))
# we need to define the pairs as the pairs of adjacent words in a text (we can choose 'newes' )
stopwords= nltk.corpus.stopwords.words('english')
# we also need to define stopword category
fdist = FreqDist([w for w in bigrams if w[0] not in stopwords and w[1] not in stopwords])
# then we define fdist as frequency distribution of pairs that their fist and second words are not stopwords
print (fdist.most_common (50))
# finally we print 50 most frequent bigrams (the result does not contain pairs with words such as 'the', but there are still instances of 'The' with uppercase letters 
# as the intial words of the sentences )
