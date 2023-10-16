import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# Function to evaluate model
def model_evaluate(model, X_test, y_test, verbose=0):
    score = model.evaluate(X_test, y_test, verbose=verbose)
    return score

# Function to predict on test data
def predict(model,test_data):
    predictions = np.argmax(model.predict(test_data), axis=-1)
    return predictions
 
# Function for Confusion matrix
def confusion_mat(test_data,predictions):
    conf_mat=confusion_matrix(test_data, predictions)
    return conf_mat

#Function for Classification matrix
def classification_mat(test_data,predictions):
    class_mat= classification_report(test_data, predictions)
    return class_mat


# Model performance during training and validation:
def model_performance(model):
    training_metrics = pd.DataFrame(model.history.history)
    return training_metrics