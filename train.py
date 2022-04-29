"""
This script will take the training output of sample.py as the input file and learn either a model 
from sklearn's MultinomialNB or SVC (with a linear kernel). It will save the model to a file. 
It is intended to be run from the command line with 3 arguments: name of the training file, 
which model(MultinomialNB or SVC) and the name of the file where to save the output.

For example: python3 train.py train_filename svc svc_modelfile
"""
import argparse
import pickle
import time
import numpy as np
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB

parser = argparse.ArgumentParser()
parser.add_argument("training_file", help="File with training data")
parser.add_argument("model", help="The chosen model")
parser.add_argument("output_file", help="Name of the file to save output")

args = parser.parse_args()


def get_training_data(data):
    """ This function opens a gzipped file and loads it."""
    with open(data, 'rb') as f:
        train_data = pickle.load(f)

    return train_data


def fix_data(file):
    """ This function fixes the data for training. Returns two arrays"""
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

    train_x = np.array(vectors)
    train_y = np.array(consonant_list)

    return train_x, train_y



def train_model(train_x, train_y, model):
    """ This function learns either NB model or SVC model and returns the model """
    model_name = model.lower()
    if model_name == 'svc':
        clf = svm.SVC(kernel='linear', probability=True)
        clf.fit(train_x, train_y)

        return clf

    elif model_name == 'nb':
        clf = MultinomialNB()
        clf.fit(train_x, train_y)

        return clf

    else:
        print("You can choose between MultinomialNB or SVC")
        
    
        
def save_model(trained_model, output):
    """ This function saves the model to a file with a given name. """
    with open(output, 'wb') as f:  # pickle from https://docs.python.org/3/library/pickle.html
        pickle.dump(trained_model, f)

    return (print("Data saved in file"))



if __name__ == '__main__':
    start = time.process_time()  
    training_data_file = get_training_data(args.training_file)
    train_x, train_y = fix_data(training_data_file)
    model_to_save = train_model(train_x, train_y, args.model)
    save_model(model_to_save, args.output_file)
    print("\nDone in", time.process_time() - start, "seconds")
