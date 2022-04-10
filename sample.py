import argparse
import gzip
import random
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="The file you want to make in to samples, a gz file")
parser.add_argument("nr_of_samples", help="The number of samples you want", type=int)
parser.add_argument("train_test_split", help="Percentage of the train/test set, 20 will give 20% for testing and 80% for training", type=int)
parser.add_argument("train_file", help="Where training data is saved")
parser.add_argument("test_file", help="Where testing data is saved")
args = parser.parse_args()

consonants = sorted(
    ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])


def sample_lines(file, lines):
    unzipped_file = gzip.open(file, 'rt')
    samples = []
    contents = unzipped_file.readlines()
    randomized_content = random.sample(contents, k=lines)
    for line in randomized_content:
        ab_lines = has_numbers(line)
        if not ab_lines:
            sample_line = line.strip().lower()
            samples.append(sample_line)
        else:
            pass

    return samples


def has_numbers(line):  # helper function to not get digits
    return any(char.isdigit() for char in line)


def create_samples(lines_sample):
    global next_cons
    new_samples = []
    for line in lines_sample:
        for i in range(0, len(line) - 5):
            char_1 = line[i] + "_1"
            char_2 = line[i + 1] + "_2"
            char_3 = line[i + 2] + "_3"
            char_4 = line[i + 3] + "_4"
            for char in line[i + 4]:
                if char in consonants:
                    next_cons = char
                else:
                    continue
                cons_samples = (char_1, char_2, char_3, char_4, next_cons)
                new_samples.append(cons_samples)

    return new_samples


def split_samples(sample_list, test_percent):
    train_percent = 100 - test_percent
    train_data = sample_list[train_percent:]
    test_data = sample_list[:test_percent]

    return train_data, test_data


def save_samples(train_data, test_data, train_file, test_file):
    with open(train_file, 'wb') as f:  # pickle from https://docs.python.org/3/library/pickle.html
        pickle.dump(train_data, f)
    with open(test_file, 'wb') as f:
        pickle.dump(test_data, f)

    return "Data saved in files"


if __name__ == "__main__":
    sampled_lines = sample_lines(args.input_file, args.nr_of_samples)
   # sampled_lines = sample_lines("UN-english.txt.gz", 10)
    get_samples = create_samples(sampled_lines)
   # get_samples = create_samples(sampled_lines)
    samples_list = get_samples
   # training_data, test_data = split_samples(samples_list, 20)
    training_data, test_data = split_samples(samples_list, args.train_test_split)
   # save_data = save_samples(training_data, test_data)
    save_data = save_samples(training_data, test_data, args.train_file, args.test_file)
    print(save_data)
