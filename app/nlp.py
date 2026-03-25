import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
import pickle
from .dataset import train_data

df = pd.DataFrame(train_data, columns=["text", "intent"])
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
Y = df["intent"]

model = LogisticRegression()
model.fit(X,Y)

with open("intent_model.pkl", "wb") as f: 
    pickle.dump((vectorizer, model), f)
    
def classify_intent(texto):
    with open("intent_model.pkl", "rb") as f: 
        vectorizer, model = pickle.load(f)
    X = vectorizer.transform([texto])
    return model.predict(X)[0]