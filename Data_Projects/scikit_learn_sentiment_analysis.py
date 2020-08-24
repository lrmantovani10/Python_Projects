import json, pickle, os, re
import random as rd
from sklearn import svm
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from autocorrect import Speller
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
        temp_list = list()
        for l in custom_list:
            temp_list+=l[:mix_list[0]]

        self.samples = temp_list
        rd.shuffle(self.samples)
    
    def feedback(self):
        return [x.feedback for x in self.samples]
    def feels(self):
        return [x.feeling for x in self.samples]


def get_words(m_f):
    #Very simple text correcter for Python - this can be substituted for
    # Sympspellpy or removed to significantly decrease compiling time.
    spell = Speller(lang='en')
    with open(m_f) as f:
        for line in f:
            rtng = json.loads(line)
            corrected_text = rtng['reviewText'].lower()
            #Removing special characters, numbers, etc.
            corrected_text = re.sub('[^a-zA-Z]', '', corrected_text)
            corrected_text = re.sub(r'\s+', ' ', corrected_text)
            corrected_text = spell(corrected_text)
            thoughts.append(Review(corrected_text, rtng['overall'], rtng['summary']))
for fily in ['Books_reviews.json','Books_small_10000.json']:
      get_words(fily)
# --- Preparing the Model
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

vectorizer = TfidfVectorizer(sublinear_tf=True,strip_accents='unicode',ngram_range=(1,2))
train_x_vectors = vectorizer.fit_transform(train_x)
test_x_vectors = vectorizer.transform(test_x)

# GridSearch and Spacy can also be sued to maximize the model's accuracy often at the
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
print('F1 Score: '+str(f1_score(test_y, clf.predict(test_x_vectors), average=None, labels = ['Good','Medium', 'Bad'])))

#Testing the model

def interaction():
    test_list = list()
    test = input('Enter a sentence for the model to predict sentiment: ')
    test_list.append(test)
    n_test = vectorizer.transform(test_list)
    print("Result for '{}' :".format(test),clf.predict(n_test))
    interaction()
interaction()
