from django.db import models

# Create your models here.
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords


data = pd.read_csv("sneakers_Reviews_Dataset.csv", delimiter=";")
data.head()
data.count()
data.isnull().sum()
data.info()
data.describe()
data['rating'].value_counts()
data['review_text'].value_counts()

column = ['timestamp', 'review_id', 'user_id']
df = data.drop(columns=column, axis=1)

pattern = r'[^A-Za-z0-9\s]+'
df['review_text'] = df['review_text'].str.replace(pattern, '', regex=True)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()  
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)
df['review_text'] = df['review_text'].apply(remove_stopwords)

df['review_text'] = df['review_text'].str.lower()

replace_map = {'review_text': {'love sneakers': 1, 'buy': 2, 'recommend': 3, 'falling apart week': 4,
                                  'uncomfortable': 5, 'highly recommend': 6, 'poor quality': 7, 'great quality': 8, 'comfortable': 9,
                                  'waste money': 10, 'average sneakers': 11, 'decent quality': 12, 'comfortable durable': 13, 'okay': 14}}
replace_map
df.replace(replace_map, inplace=True)

replace_map = {'rating': {1 : 'negative' , 2 : 'negative', 3 : 'neutral', 4 : 'positive', 5 : 'positive'}}
replace_map
df.replace(replace_map, inplace=True)


X = df.drop(['rating'], axis=1)
y = df['rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logreg_classifier = LogisticRegression()
logreg_classifier.fit(X_train, y_train)
y2 = logreg_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y2)
precision = precision_score(y_test, y2, average='weighted')
recall = recall_score(y_test, y2, average='weighted')
F1_score = f1_score(y_test, y2, average='weighted')

print('Accuracy: ', accuracy)
print('Precision: ', precision)
print('Recall: ', recall)
print('F1 Score: ', F1_score)