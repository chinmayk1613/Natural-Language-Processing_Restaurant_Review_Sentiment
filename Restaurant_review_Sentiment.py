#Natural Language Processing

#Bag of words model

#Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
def restaurant_review_sentiment():
    #Importing the Dataset
    dataset=pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
    #Cleaning the texts
    import re
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords #for stopwords
    from nltk.stem.porter import PorterStemmer #for stamming to each of the word....to find the root of word
    corpus_list = []
    for i in range(0,1000):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not  word in set(stopwords.words('english'))]
        #Stamming...taking the root of word eg. loved--->love
        review = ' '.join(review)
        corpus_list.append(review)


    #creating the bag of words model
    from sklearn.feature_extraction.text import CountVectorizer # to create sparse matrix
    cv = CountVectorizer(max_features = 1500) # for cleaning the text which we did above
    X = cv.fit_transform(corpus_list).toarray()
    y = dataset.iloc[:, 1].values

    #Splitting dataset into train and test data
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)


    #Fitting the Naive Bayes classifier to the training set
    from sklearn.naive_bayes import GaussianNB
    classifier=GaussianNB()
    classifier.fit(X_train,y_train)

    #Predicting the test set result
    y_pred=classifier.predict(X_test)
    print(y_pred)



    #Making the confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm=confusion_matrix(y_test,y_pred)
    print(cm)
    (55+91)/200

    from mlxtend.plotting import plot_confusion_matrix
    import matplotlib.pyplot as plt


    fig, ax = plot_confusion_matrix(conf_mat=cm)
    plt.show()

if __name__=='__main__':
    restaurant_review_sentiment()