"""
This script will load the model output of train.py and the test sample output of test.py and calculate accuracy, precision, recall, and F-measure and print these out to the terminal.

Example on how to run: python3 test.py svc_model test_datafile macro
"""

import pickle
import argparse
from sklearn import metrics
import numpy as np
import time
import random

parser = argparse.ArgumentParser()
parser.add_argument("model_file", help="Name of file with model saved in it")
parser.add_argument("test_data", help="Name of test data")
parser.add_argument("avg_type", help="Micro or macro averaging")

args = parser.parse_args()

def get_model(data): #data is train_output from train.py
    with open(data, 'rb') as f:
        model = pickle.load(f)
    
    return model


def get_testdata(data):  #output of sample.py
    with open(data, 'rb') as f:
        test_data = pickle.load(f)

    return test_data


def fix_data(file):
    """ This function fixes the data for testing. """
    column_list = []
    consonant_list = []
    vectors = []
    for chars, cons in file:
        column_list.append(chars)
    flattened_list = [item for sublist in column_list for item in sublist]
    flattened_list.append("prediction")
    
    for characters, consonant in file:
        v = []
        for item in flattened_list:
            if item != "prediction":
                if item in characters:
                    v.append(1)
                elif item not in characters:
                    v.append(0)
                else:
                    continue
        consonant_list.append(consonant)
        vectors.append(v)

    test_x = np.array(vectors)
    test_y = np.array(consonant_list)
    
    return test_x, test_y


def calculate_metrics(model, test_x, test_y, avg_type):
    model.fit(test_x, test_y)
    y_pred = model.predict(test_x)
    if avg_type == 'micro' or 'macro':
        accuracy = metrics.accuracy_score(test_y, y_pred)
        precision = metrics.precision_score(test_y, y_pred, average=avg_type, zero_division=0)
        recall = metrics.recall_score(test_y, y_pred, average=avg_type, zero_division=0)
        f1 = metrics.f1_score(test_y, y_pred, average=avg_type, zero_division=0)
    else:
        print("Please choose another averaging type")
    
    return accuracy, precision, recall, f1
    

if __name__ == '__main__':
    start = time.process_time()
    model = get_model(args.model_file)
    get_test_data = get_testdata(args.test_data)
    test_x, test_y = fix_data(get_test_data)
    accuracy, precision, recall, f1 = calculate_metrics(model, test_x, test_y, args.avg_type)
    output = "Accuracy: {acc} \nPrecision: {prec} \nRecall: {rec} \nF1 score: {f1_score}".format(acc=accuracy, prec=precision, rec=recall, f1_score=f1)
    print(output)
    time_taken = time.process_time() - start
    print("\nDone in {:.4f} seconds".format(time_taken))
