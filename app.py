from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

app = Flask(__name__)

# Load doctor data
doctors_df = pd.read_csv('data/doctors.csv')

# Load the trained model
with open('models/doctor_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle symptom input and recommend doctors
@app.route('/recommend', methods=['POST'])
def recommend():
    symptoms = request.form.get('symptoms')

    # Transform input symptoms using TF-IDF vectorizer
    symptoms_vector = model['tfidf_vectorizer'].transform([symptoms])

    # Predict doctor recommendations using trained model
    doctor_indices = model['model'].kneighbors(symptoms_vector)[1][0]
    recommended_doctors = doctors_df.iloc[doctor_indices]['DoctorName'].tolist()

    return render_template('index.html', symptoms=symptoms, recommended_doctors=recommended_doctors)

if __name__ == '__main__':
    app.run(debug=True)
