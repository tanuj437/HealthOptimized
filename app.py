from flask import Flask, render_template, request, redirect, session
import csv
import os
import prediction
from time import sleep
app = Flask(__name__)
app.secret_key = '112nvroe23'


def check_existing_user(email):
    with open("user_data.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if email in row:
                return True
    return False

def store_user_details(name, email):
    with open("user_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email])

def update_user_file(name, email, form_data):
    with open("user_details.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email] + list(form_data.values()))

def get_user_data(name, email):
    with open("user_details.csv", "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader if row['Name'] == name and row['Email'] == email]
    return data





@app.route('/'or '')
def login():
    session.clear()
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'name' in session and 'email' in session:
        name = session['name']
        email = session['email']
        if check_existing_user(email):
            user_data = get_user_data(name, email)
            return render_template('home.html', name=name, email=email, user_data=user_data)
    
    if request.method == 'POST':
        name = request.form.get("Name")
        email = request.form.get("email")
        session.clear()  # Clear existing session data
        session['name'] = name
        session['email'] = email
        if check_existing_user(email):
            user_data = get_user_data(name, email)
            return render_template('home.html', name=name, email=email, user_data=user_data)
        else:
            store_user_details(name, email)
            return render_template('form.html', name=name, email=email)
    else:
        session.clear()  # Clear existing session data
        return redirect('/login')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = session.get('name')
        email = session.get('email')
        form_data = {
            'Age': request.form['Age'],
            'Weight': request.form['Weight'],
            'Height': request.form['Height'],
            'Sex': request.form['Sex'],
            'HighBP': request.form['HighBP'],
            'HighChol': request.form['HighChol'],
            'CholCheck': request.form['CholCheck'],
            'BMI': request.form['BMI'],
            'Smoker': request.form['Smoker'],
            'Stroke': request.form['Stroke'],
            'PhysActivity': request.form['PhysActivity'],
            'Fruits': request.form['Fruits'],
            'Veggies': request.form['Veggies'],
            'HvyAlcoholConsump': request.form['HvyAlcoholConsump'],
            'AnyHealthcare': request.form['AnyHealthcare'],
            'NoDocbcCos': request.form['NoDocbcCos'],
            'GenHlth': request.form['GenHlth'],
            'MentHlth': request.form['MentHlth'],
            'PhysHlth': request.form['PhysHlth'],
            'DiffWalk': request.form['DiffWalk'],
            'AirPollution': request.form['AirPollution'],
            'AlcoholUse': request.form['AlcoholUse'],
            'DustAllergy': request.form['DustAllergy'],
            'OccuPationalHazards': request.form['OccuPationalHazards'],
            'GeneticRisk': request.form['GeneticRisk'],
            'ChronicLungDisease': request.form['ChronicLungDisease'],
            'BalancedDiet': request.form['BalancedDiet'],
            'Obesity': request.form['Obesity'],
            'Smoking': request.form['Smoking'],
            'PassiveSmoker': request.form['PassiveSmoker'],
            'ChestPain': request.form['ChestPain'],
            'CoughingofBlood': request.form['CoughingofBlood'],
            'Fatigue': request.form['Fatigue'],
            'WeightLoss': request.form['WeightLoss'],
            'ShortnessofBreath': request.form['ShortnessofBreath'],
            'Wheezing': request.form['Wheezing'],
            'SwallowingDifficulty': request.form['SwallowingDifficulty'],
            'ClubbingofFingerNails': request.form['ClubbingofFingerNails'],
            'FrequentCold': request.form['FrequentCold'],
            'DryCough': request.form['DryCough'],
            'Snoring': request.form['Snoring'],
            'Hypertension': request.form['Hypertension'],
            'heartdisease':0,
            'EverMarried': request.form['EverMarried'],
            'WorkType': request.form['WorkType'],
            'AvgGulocoseLevel': request.form["AvgGulocoseLevel"],
            'SmokingStatus': request.form['SmokingStatus']

        }
        if check_existing_user(email):
            update_user_file(name, email, form_data)
        else:
            store_user_details(name, email)
            update_user_file(name, email, form_data)
        return redirect('/home')
@app.route('/cancerrisk')
def cancerrisk():
    name = session.get('name')
    email = session.get('email')
    user_data = get_user_data(name,email)
    cancer=prediction.cancer(user_data[0])
    return render_template('Cancer.html',user_data=user_data[0],cancer=cancer)
@app.route('/Heartrisk')
def heartrisk():
    name = session.get('name')
    email = session.get('email')
    user_data = get_user_data(name,email)
    heart=prediction.heart(user_data[0])
    return render_template('Heart.html',user_data=user_data[0],heart=heart)
@app.route('/diabetesrisk')
def diabetesrisk():
    name = session.get('name')
    email = session.get('email')
    user_data = get_user_data(name,email)
    diabetes=prediction.diabetes(user_data[0])
    return render_template('Diabetes.html',user_data=user_data[0],diabetes=diabetes)

if __name__ == '__main__':
    app.run(port=6969, debug=True)
