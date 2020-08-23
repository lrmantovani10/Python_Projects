import json, pickle, os, spacy
import random as rd
from html import unescape
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB
from sklearn.feature_extraction.text import TfidfVectorizer
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
            return 'Bad'
        elif self.overall==3:
            return 'Medium'
        else:
            return 'Good'
class Arrange:
    def __init__(self, samples):
        self.samples = samples

    def flatten(self):
        custom_list = list()
        for el in ['Bad', 'Medium', 'Good']:
            custom_list.append(list(filter(lambda x: x.feeling == el, self.samples)))
        #See which list is the smallest
        mix_list = [len(k) for k in custom_list]
        mix_list.sort()
        #Equalizing list lengths and appending remaining data to test data to not waste it
        temp_list = list()
        for l in custom_list:
            temp_list+=l[:mix_list[0]]

        self.samples = temp_list
        rd.shuffle(self.samples)
    
    def feedback(self):
        return [x.feedback for x in self.samples]
    def feels(self):
        return [x.feeling for x in self.samples]
        
# Vectorizing using SpaCy
class My_Vec(TfidfVectorizer): 
    def build_analyzer(self):  
        # load stop words using Tfidf's built-in method
        stop_words = self.get_stop_words()
        def analyzer(doc):
            nlp = spacy.load('en_core_web_lg')
            # apply the preprocessing and tokenzation steps
            doc_clean = unescape(doc).lower()
            tokens = nlp(doc_clean)
            lemmatized_tokens = [token.lemma_ for token in tokens]
            return(self._word_ngrams(lemmatized_tokens, stop_words))
        return(analyzer)

for m_f in ['Books_reviews.json','Books_small_10000.json']:
    with open(m_f) as f:
        for line in f:
            rtng = json.loads(line)
            thoughts.append(Review(rtng['reviewText'], rtng['overall'], rtng['summary']))
        
# --- Preparing the Model

training, test = train_test_split(thoughts, test_size=0.25, random_state=42)

test_data = Arrange(test)
train_data = Arrange(training)
train_data.flatten()
test_data.flatten()
train_x = train_data.feedback()
train_y = train_data.feels()
test_x = test_data.feedback()
test_y = test_data.feels()

rd.shuffle(test_data.samples)

vectorizer = TfidfVectorizer(ngram_range=(1,2),stop_words='english')
#Using the SpaCy - featuring vectorizer
vec1  = My_Vec()
# Standard scikit learn Tfidf vectorizer
train_x_vectors = vectorizer.fit_transform(train_x)
test_x_vectors = vectorizer.transform(test_x)
#SpaCy
train_x_vectors1 = vec1.fit_transform(train_x)
test_x_vectors1 = vec1.transform(test_x)

if not os.path.exists('./Image_Recognition/Classifier_Saved.pkl'):
    clf = ComplementNB()
    #Saving Model
    with open('Classifier_Saved.pkl', 'wb') as file:
        pickle.dump(clf, file)
else:
    #Loading Model
    with open('Classifier_Saved.pkl', 'rb') as file:
        clf = pickle.load(file)

# Predict if specific sample is good/bad clf.predict(test_x_vectors[5])
clf.fit(train_x_vectors, train_y)
print(clf.score(test_x_vectors, test_y))
print(f1_score(test_y, clf.predict(test_x_vectors), average=None, labels = ['Good','Medium', 'Bad']))

#Results
print(clf.score(test_x_vectors1, test_y))
print(f1_score(test_y, clf.predict(test_x_vectors1), average=None, labels = ['Good','Medium', 'Bad']))

#Testing the model
def interaction():
    test_list = list()
    test = input('Enter a sentence for the model to predict sentiment: ')
    test_list.append(test)
    n_test = vectorizer.transform(test_list)
    print("Result for '{}' :".format(test),clf.predict(n_test))
    interaction()
interaction()