from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)

model1 = pickle.load(open('Diabetes_Model.pkl', 'rb'))
model2 = pickle.load(open('Heart_Model.pkl', 'rb'))
model3 = pickle.load(open('Parkinson_Model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

#  ------------- For diabetes page to open --------------------

@app.route('/diabetes-prediction-page')
def diabetes_page():
    return render_template('Diabetes.html')


@app.route('/handle-click')
def handle_click():
    return redirect('/diabetes-prediction-page')

#  ------------- For Heart page to open --------------------

@app.route('/heart-disease-prediction-page')
def heart_page():
    return render_template('Heart.html')


@app.route('/handle-click1')
def handle_click1():
    return redirect('/heart-disease-prediction-page')

#  --------------------- For Parkinson page to open ------------------------

@app.route('/parkinson-disease-prediction-page')
def parkinson_page():
    return render_template('Parkinson.html')


@app.route('/handle-click2')
def handle_click2():
    return redirect('/parkinson-disease-prediction-page')

# ------------------ For BMI Page to open --------------------------

@app.route('/body-mass-index-calculator-page')
def bmi_page():
    return render_template('BMI.html')


@app.route('/handle-click3')
def handle_click3():
    return redirect('/body-mass-index-calculator-page')

@app.route('/contact-us-page')
def contact():
    return render_template('contactus.html')

@app.route('/About-us-page')
def about():
    return render_template('aboutUs.html')

# ---------------------- Diabetes Predictions ---------------------------


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    Glucose = int(request.form['Glucose'])
    Blood = int(request.form['Blood'])
    Insulin = int(request.form['Insulin'])
    bmi = int(request.form['BMI'])
    age = int(request.form['Age'])

    output = model1.predict_proba([[Glucose, Blood, Insulin, bmi, age]])
    probas_yes = output[:, 1]
    probas_no = output[:, 0]
    percent_yes = sum(probas_yes) / len(probas_yes) * 100
    percent_no = sum(probas_no) / len(probas_no) * 100

    return render_template('Diabetes.html', yes=percent_yes, no=percent_no)

# ---------------------- Heart Predictions ---------------------------


@app.route('/prediction1', methods=['POST', 'GET'])
def prediction1():
    age1 = int(request.form['age'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['tbps'])
    cholestrol = int(request.form['chol'])
    thal = int(request.form['thal'])
    slope = int(request.form['slope'])

    output1 = model2.predict_proba([[age1, cp, trestbps, cholestrol, thal, slope]])
    probas_yes1 = output1[:, 1]
    probas_no1 = output1[:, 0]
    percent_yes1 = sum(probas_yes1) / len(probas_yes1) * 100
    percent_no1 = sum(probas_no1) / len(probas_no1) * 100

    return render_template('Heart.html', yes1=percent_yes1, no1=percent_no1)

# ---------------------- Parkinson Predictions ---------------------------


@app.route('/prediction2', methods=['POST', 'GET'])
def prediction2():
    mdvpfhi = float(request.form['mdvpfhi'])
    mdvpflo = float(request.form['mdvpflo'])
    mdvpjitter = float(request.form['mdvpjitter'])
    mdvpshi = float(request.form['mdvpshi'])
    mdvpshidb = float(request.form['mdvpshidb'])
    shiq3 = float(request.form['shiq3'])
    shiq5 = float(request.form['shiq5'])
    mdvpapq = float(request.form['mdvpapq'])
    shidda = float(request.form['shidda'])
    rpde = float(request.form['rpde'])
    spread1 = float(request.form['spread1'])
    spread2 = float(request.form['spread2'])
    d2 = float(request.form['d2'])
    ppe = float(request.form['ppe'])

    output2 = model3.predict_proba([[mdvpfhi, mdvpflo, mdvpjitter, mdvpshi, mdvpshidb,shiq3, shiq5, mdvpapq, shidda, rpde, spread1, spread2, d2, ppe]])
    probas_yes2 = output2[:, 1]
    probas_no2 = output2[:, 0]
    percent_yes2 = sum(probas_yes2) / len(probas_yes2) * 100
    percent_no2 = sum(probas_no2) / len(probas_no2) * 100

    return render_template('Parkinson.html', yes2=percent_yes2, no2=percent_no2)

# ---------------------- Main Class ---------------------------


if __name__ == '__main__':
    app.run(debug=True)
