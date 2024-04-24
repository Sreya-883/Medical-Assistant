import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

def preprocess_dataset(file_path):
    # Load the disease and symptoms dataset
    df = pd.read_csv(file_path)

    # Data cleaning and preprocessing
    df = df[['Disease', 'Symptom']]
    df.dropna(inplace=True)
    df['Symptom'] = df['Symptom'].str.lower()

    return df

def train_model(df):
    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the symptom data
    symptom_vectors = vectorizer.fit_transform(df['Symptom'])

    # Train a simple linear kernel model for similarity
    model = {
        'tfidf_vectorizer': vectorizer,
        'model': linear_kernel(symptom_vectors, symptom_vectors)
    }

    return model

def save_model(model, file_path):
    # Save the trained model using pickle
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)

    print("Model training completed and saved.")

def main():
    # Specify file paths
    dataset_path = 'data/disease_symptom.csv'
    model_path = 'models/doctor_recommendation_model.pkl'

    # Preprocess dataset
    df = preprocess_dataset(dataset_path)

    # Train model
    model = train_model(df)

    # Save model
    save_model(model, model_path)

if __name__ == '__main__':
    main()
