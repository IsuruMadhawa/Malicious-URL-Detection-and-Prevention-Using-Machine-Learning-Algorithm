import pickle
from flask import Flask, request, jsonify
import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from tld import get_tld, is_tld

with open('mycode.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the data from the request
    data = request.json

    # Perform any necessary preprocessing on the data

    # Make predictions using the loaded model
    predictions = model.predict(data)

    # Return the predicted results
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run()

