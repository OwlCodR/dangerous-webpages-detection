from pandas import read_csv, DataFrame, Series
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score 
from sklearn.metrics import precision_recall_curve, classification_report
from sklearn.model_selection import cross_validate
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib

from sklearn.svm import SVC, LinearSVC, LinearSVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB, CategoricalNB

import matplotlib.pyplot as plt
import seaborn as sns
import pylab as pl
import numpy as np
from random import shuffle


class ML:

    def __init__(self):
        self.dataset_path = 'python/server/dataset/big_dataset4.csv'
        self.test_dataset_path = 'python/server/dataset/small_dataset2.csv'
    
    def make_chart(self, text_clf):
        sns.set(font_scale=1.5)
        sns.set_color_codes("muted")

        plt.figure(figsize=(10, 8))
        fpr, tpr, thresholds = roc_curve(self.test_labels, text_clf.predict_proba(self.test_sentences)[:,1], pos_label=1)
        lw = 2
        plt.plot(fpr, tpr, lw=lw, label='ROC curve ')
        plt.plot([0, 1], [0, 1])
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC curve')
        plt.show()

    def report(self, text_clf, is_make_chart):
        predictions = text_clf.predict(self.test_sentences)
        print('->', accuracy_score(predictions, self.test_labels))

        #mask = np.logical_not(np.equal(self.test_labels, predictions))
        #print(f"Elements wrong classified: \n{np.array(self.test_sentences)[mask]}\n")

        report = classification_report(self.test_labels, predictions)
        print(report)
        if is_make_chart:
            self.make_chart(text_clf)


    def mix_datasets(self):
        dic = {self.sentences[i]:self.labels[i] for i in range(len(self.sentences))}
        test_dic = {self.test_sentences[i]:self.test_labels[i] for i in range(len(self.test_sentences))}

        arr = list(dic.items())
        shuffle(arr)
        dic = dict(arr)

        test_arr = list(test_dic.items())
        shuffle(test_arr)
        test_dic = dict(test_arr)

        self.sentences = [x for x in dic.keys()]
        self.labels = [x for x in dic.values()]

        self.test_sentences = [x for x in test_dic.keys()]
        self.test_labels = [x for x in test_dic.values()]


    def read_datasets(self):
        learn_data = read_csv(self.dataset_path, sep=';')
        test_data = read_csv(self.test_dataset_path, sep=';')

        self.sentences = learn_data[learn_data.columns[0]]
        self.labels = learn_data[learn_data.columns[1]]

        self.test_sentences = test_data[test_data.columns[0]]
        self.test_labels = test_data[test_data.columns[1]]

    def learn_clf(self, vectorizer, classifier, is_make_chart):
        text_clf = Pipeline([
                     ('countVec', vectorizer),
                     ('clf', classifier)
                     ])
        print('Start learning...')
        text_clf.fit(self.sentences, self.labels)
        print('Finish learning...')
        self.report(text_clf, is_make_chart)
        return text_clf

    def learn(self):
        self.read_datasets()
        self.mix_datasets()
        self.nb = self.learn_clf(TfidfVectorizer(), BernoulliNB(), True)
        #self.svc = self.learn_clf(TfidfVectorizer(), SVC(probability=True), True)
        self.lsvc = self.learn_clf(TfidfVectorizer(), LinearSVC(), False)
        self.sgd = self.learn_clf(TfidfVectorizer(), SGDClassifier(), False)

    def save_all_clf(self):
        main_path = 'python/server/ml_models/'
        joblib.dump(self.nb, main_path + 'nb.pkl') 
        #joblib.dump(self.svc, main_path + 'svc.pkl') 
        joblib.dump(self.lsvc, main_path + 'lsvc.pkl') 
        joblib.dump(self.sgd, main_path + 'sgd.pkl') 
        
    def load_all_clf(self):
        main_path = 'python/server/ml_models/'
        self.nb = joblib.load(main_path + 'nb.pkl') 
        #self.svc = joblib.load(main_path + 'svc.pkl') 
        self.lsvc = joblib.load(main_path + 'lsvc.pkl') 
        self.sgd = joblib.load(main_path + 'sgd.pkl') 
    
if __name__ == '__main__':
    ml = ML()
    #ml.learn()
    #ml.save_all_clf()

    ml.load_all_clf()