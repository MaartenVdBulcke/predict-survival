from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pc = request.form['passengerclass']
        sex = request.form['sex']
        age = request.form['age']
        siblings = request.form['siblings']
        fare = request.form['fare']
        pred = model.predict([[pc, sex, age, siblings, fare]])
        if pred[0] == 0:
            string = str('You did not survive')
        else:
            string = str('You got lucky and survived, but you are not the same person as before')
        return render_template('index.html', pred=string)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()