"""
This script will take gzipped file and create samples of it. It should run from the command line with 5 commands; the input file, how many samples to make, percentage of test size for training and testing splits, name of the training file and name of the testing file.

For example: python3 sample.py example.txt.gz 100 20 train_filename test_filename

"""

import argparse
import gzip
import random
import pickle
import time

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="The file you want to make in to samples, a gz file")
parser.add_argument("nr_of_samples", help="The number of samples you want", type=int)
parser.add_argument("train_test_split", help="Percentage of the train/test set, 20 will give 20% for testing and 80% for training", type=int)
parser.add_argument("train_file", help="Where training data is saved")
parser.add_argument("test_file", help="Where testing data is saved")
args = parser.parse_args()

consonants = sorted(
    ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])

def sample_lines(file):
    """ This function opens a gzipped file and reads it. It looks for non digits and returns a list of samples"""
    
    unzipped_file = gzip.open(file, 'rt')
    samples = []
    contents = unzipped_file.readlines()
    for line in contents:
        sample_line = line.strip().lower()
        samples.append(sample_line)

    return samples


def create_samples(lines_sample, nr_of_samples):
    """This function takes a list of samples, randomizes it and returns an n sample long list in the format: 
       (x_1, y_2, z_3, w_4), consonant).
    """
    randomized_content = random.sample(lines_sample, k=nr_of_samples)
    new_samples = []
    for line in randomized_content:
        for i in range(0, len(line) - 5):
            char_1, char_2, char_3, char_4 = (line[i] + "_1", line[i + 1] + "_2", line[i + 2] + "_3", line[i + 3] + "_4")
            characters = char_1, char_2, char_3, char_4
            for char in line[i + 4:]:
                if char in consonants:
                    next_cons = char
                else:
                    continue
                cons_samples = (characters, next_cons)
                new_samples.append(cons_samples)
                if len(new_samples) == nr_of_samples:
                    return new_samples
           
               
def split_samples(sample_list, test_percent):
    """This function divides samples into a training set and a test set based on test percent.
    
        If test percent is 20% the split will be 80/20.
    """
    percent = int(round(len(sample_list) * (test_percent/100)))
    train_data = sample_list[percent:]
    test_data = sample_list[:percent]
    

    return train_data, test_data


def save_samples(train_data, test_data, train_file, test_file):
    """ This function will take the training and test data from split_samples and upload them to new files. """
    with open(train_file, 'wb') as f:  # pickle from https://docs.python.org/3/library/pickle.html
        pickle.dump(train_data, f)
    with open(test_file, 'wb') as f:
        pickle.dump(test_data, f)

    return "Data saved in files"
        
      
if __name__ == "__main__":
    start = time.process_time()    
    sampled_lines = sample_lines(args.input_file)
    full_samples = create_samples(sampled_lines, args.nr_of_samples)
    training_data, test_data = split_samples(full_samples, args.train_test_split)
    save_data = save_samples(training_data, test_data, args.train_file, args.test_file)
    print("\nDone in", time.process_time() - start, "seconds")
    
