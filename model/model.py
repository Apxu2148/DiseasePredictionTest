import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'heart.csv')
    data = pd.read_csv(data_path)
    return data

def train_model(data):
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    model = LogisticRegression(max_iter = 3000)
    model.fit(X_train, y_train)
    return model

def save_model(model):
    model_path = os.path.join(os.path.dirname(__file__), 'logistic_regression_model.pkl')
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

def main():
    data = load_data()
    model = train_model(data)
    save_model(model)
    print("Model trained and saved to file 'logistic_regression_model.pkl'.")

if __name__ == "__main__":
    main()
