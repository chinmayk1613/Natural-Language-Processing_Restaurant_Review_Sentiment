# Natural-Language-Processing_Restaurant_Review_Sentiment

<code>__Natural Language Processing__</code>


Data comes in various format including texts. We as a human speak many languages and genrate data in unstructured way but to process that data and extract meaningfull information using computer requires structures data. To develop such applications to process natural language we required to convert the unstructred and ambiguous data in strucutred way that computer can understand and process it. This process of converting unstructures to structures data is known as Natural Language Processing which is again a subfield of Artificial Intelligence which allows computers to understand and process human language. The main task of such models is to analyze and process huge amount of natural language data.To build the model we have to pre-process the data which gives structured data to computer, below are the some steps which involve in data pre-processing.

<code>__1. Elimination Of Stopwords:__</code> This is the list of words which does not add meaning to the setences. So we have to remove the words which are present in our setences from the stopword list.

<code>__2. Stamming Process:__</code> This is the process where we found the root of word. For ex. If we have word 'Taken' then using this stamming process that word convert to its root that is 'Take' so it will convert it into original form of word.

<code>__3. Bag of Words Model:__</code> Bag of words model is the heart of sentiment analysis. After stamming process all the words comes in root format also follwing the most important words according to stopword list. Bag of words model create the dictoanry in which key the words and value is the number of times that word is appearing in given text. The main motto of this representation is to features genration. In this way the words convert into numeric value based on its ocuurances and then it moves further to model on which it get trained.

<code>__Experiment__</code>

In this experiment restaurant review is being analyzed which are in ENGLISH natural language. They categories as Liked(Positive) symbolled as 0 and not Liked(Negative) sumbolled as 1. Here total 1000 review taken under consideration out of which 800 used for training purpose and 200 usedf for testing. After training naive bais classifier on test data this model gives 73% accuracy.

<code>__Confusion Matrix__</code>
