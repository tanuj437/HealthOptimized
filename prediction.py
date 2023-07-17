import pickle

import pickle

def cancer(user_data):
    with open("trained_model/cancer_model.pkl", 'rb') as file:
        model = pickle.load(file)

    data = [
        [
            int(user_data['Age']),
            int(user_data['Sex']),
            int(user_data['AirPollution']),
            int(user_data['AlcoholUse']),
            int(user_data['DustAllergy']),
            int(user_data['OccuPationalHazards']),
            int(user_data['GeneticRisk']),
            int(user_data['ChronicLungDisease']),
            int(user_data['BalancedDiet']),
            int(user_data['Obesity']),
            int(user_data['Smoking']),
            int(user_data['PassiveSmoker']),
            int(user_data['ChestPain']),
            int(user_data['CoughingofBlood']),
            int(user_data['Fatigue']),
            int(user_data['WeightLoss']),
            int(user_data['ShortnessofBreath']),
            int(user_data['Wheezing']),
            int(user_data['SwallowingDifficulty']),
            int(user_data['ClubbingofFingerNails']),
            int(user_data['FrequentCold']),
            int(user_data['DryCough']),
            int(user_data['Snoring'])
        ]
    ]
    
    predictions = model.predict(data)
    if predictions[0]=="High":
        return "Moderate Risk"
    else:
        return predictions[0]

def diabetes(user_data):
    with open("trained_model/diabetes.pkl", 'rb') as file:
        model = pickle.load(file)

    data = [
        [
            int(user_data['HighBP']),
            int(user_data['HighChol']),
            int(user_data['CholCheck']),
            int(user_data['BMI']),
            int(user_data['Smoker']),
            int(user_data['Stroke']),
            0,
            int(user_data['PhysActivity']),
            int(user_data['Fruits']),
            int(user_data['Veggies']),
            int(user_data['HvyAlcoholConsump']),
            int(user_data['AnyHealthcare']),
            int(user_data['NoDocbcCos']),
            int(user_data['GenHlth']),
            int(user_data['MentHlth']),
            int(user_data['PhysHlth']),
            int(user_data['DiffWalk']),
            int(user_data['Sex']),
            int(user_data['Age'])
        ]
    ]

    predictions = model.predict(data)
    
    return predictions[0]


def heart(user_data):
    with open("trained_model/heart_model.pkl", 'rb') as file:
        model = pickle.load(file)

    data = [
        [
            int(user_data['HighBP']),
            int(user_data['HighChol']),
            int(user_data['CholCheck']),
            int(user_data['BMI']),
            int(user_data['Smoker']),
            int(user_data['Stroke']),
            0 ,
            int(user_data['PhysActivity']),
            int(user_data['Fruits']),
            int(user_data['Veggies']),
            int(user_data['HvyAlcoholConsump']),
            int(user_data['AnyHealthcare']),
            int(user_data['NoDocbcCos']),
            int(user_data['GenHlth']),
            int(user_data['MentHlth']),
            int(user_data['PhysHlth']),
            int(user_data['DiffWalk']),
            int(user_data['Sex']),
            int(user_data['Age'])
        ]
    ]

    predictions = model.predict(data)
  
    return predictions[0]


def stroke(user_data):
    with open("trained_model/stroke_model.pkl", 'rb') as file:
        model = pickle.load(file)

    data = [
        [
            int(user_data['Sex']),
            int(user_data['Age']),
            int(user_data['Hypertension']),
            int(user_data['heartdisease']),
            int(user_data['EverMarried']),
            int(user_data['WorkType']),
            float(user_data['AvgGulocoseLevel']),
            float(user_data['BMI']),
            int(user_data['SmokingStatus'])
        ]
    ]

    predictions = model.predict(data)

    return predictions[0]
