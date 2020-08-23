'''
Python sentiment analysis. 
Consulted sources and further reference:
https://stackabuse.com/implementing-word2vec-with-gensim-library-in-python/
https://github.com/KeithGalli/sklearn/tree/master/data/sentiment
''' 
import json, pickle, os, nltk, re
from gensim.models import Word2Vec
#Necessary: nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
import random as rd
from nltk.corpus import stopwords
from sklearn import svm
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

thoughts = list()

# --- Managing Data
class Review:
    def __init__(self, feedback, overall, summary):
        self.feedback = feedback
        self.overall = overall
        self.summary = summary
        self.feeling = self.get_feeling()

    def get_feeling(self):
        if self.overall<=2:
            return 'Negative'
        elif self.overall==3:
            return 'Neutral'
        else:
            return 'Positive'
class Arrange:
    def __init__(self, samples):
        self.samples = samples

    def flatten(self):
        custom_list = list()
        for el in ['Negative', 'Neutral', 'Positive']:
            custom_list.append(list(filter(lambda x: x.feeling == el, self.samples)))
        #See which list is the smallest
        mix_list = [len(k) for k in custom_list]
        mix_list.sort()
        temp_list = list()
        for l in custom_list:
            temp_list+=l[:mix_list[0]]

        self.samples = temp_list
        rd.shuffle(self.samples)
    
    def feedback(self):
        return [x.feedback for x in self.samples]
    def feels(self):
        return [x.feeling for x in self.samples]

w_text = ''
def get_words(m_f):
    global thoughts, w_text
    with open(m_f) as f:
        for line in f:
            rtng = json.loads(line)
            w_text += rtng['reviewText']
            thoughts.append(Review(rtng['reviewText'], rtng['overall'], rtng['summary']))
for fily in ['Books_reviews.json','Books_small_10000.json']:
      get_words(fily)

# Preparing the Model
training, test = train_test_split(thoughts, test_size=0.248, random_state=42)
test_data = Arrange(test)
train_data = Arrange(training)
train_data.flatten()
test_data.flatten()
train_x = train_data.feedback()
train_y = train_data.feels()
test_x = test_data.feedback()
test_y = test_data.feels()
rd.shuffle(test_data.samples)

# Preprocessing - I used w_text instead of .feedback() for building the vectorizer model 
w_text = w_text.lower()
#Removing special characters, numbers, etc.
w_text = re.sub('[^a-zA-Z]', '', w_text)
w_text = re.sub(r'\s+', ' ', w_text)
# Most reviews will probbaly be a few sentences, but some can be longer.
# Thus, it is interesting to sent_tokenize them.
t_sentence = nltk.sent_tokenize(w_text)
# Removing stop words and setting up tokenized words list
t_words = list()
for ab in t_sentence:
    for element in ab:
        if element not in stopwords.words('english'):
            nltk.word_tokenize(element)
            t_words.append(element)

if not os.path.exists('./Projects/Vectorizer_Saved.pkl'):
    vectorizer = Word2Vec(t_words, min_count=2)
    #Saving Word2Vec
    with open('Vectorizer_Saved.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)
else:
    #Loading Word2Vec vectorizer
    with open('Vectorizer_Saved.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

train_x_vectors = vectorizer.fit_transform(train_x)
test_x_vectors = vectorizer.transform(test_x)

# GridSearch and Spacy can also be used to maximize the model's accuracy often at the
# expense of lower f1 scores for certain categories.

if not os.path.exists('./Projects/Classifier_Saved.pkl'):
    clf = svm.LinearSVC()
    #Saving Model
    with open('Classifier_Saved.pkl', 'wb') as file:
        pickle.dump(clf, file)
else:
    #Loading Model
    with open('Classifier_Saved.pkl', 'rb') as file:
        clf = pickle.load(file)

#Assessing classifier quality
clf.fit(train_x_vectors, train_y)
print('Overall score: '+str(clf.score(test_x_vectors, test_y)))
print('F1 Score: '+str(f1_score(test_y, clf.predict(test_x_vectors), average=None, labels = ['Positive','Neutral', 'Negative'])))

#Testing the model

def interaction():
    test_list = list()
    test = input('Enter a sentence for the model to predict sentiment: ')
    test_list.append(test)
    n_test = vectorizer.transform(test_list)
    print("Result for '{}' :".format(test),clf.predict(n_test))
    interaction()
interaction()