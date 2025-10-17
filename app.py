import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

model=pickle.load(open('best_logistic_regression_model.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def imdex():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Pregnancies	= request.form['Pregnancies']
    Glucose= request.form['Glucose']
    Insulin	= request.form['Insulin']
    BMI	= request.form['BMI']
    DiabetesPedigreeFunction= request.form['DiabetesPedigreeFunction']	
    Age= request.form['Age']

    features=np.array([[Pregnancies,Glucose,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    prediction = model.predict(features).reshape(1,-1)

    return render_template('index.html',output = prediction[0])
    pass

if __name__ == '__main__':
    app.run(debug=True)