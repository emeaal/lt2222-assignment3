def sample_lines(file):
    unzipped_file = gzip.open(file, 'rt', encoding='utf-8')
    samples = []
    contents = unzipped_file.readlines()
    #randomized_content = random.sample(contents, k=lines)
    for line in contents:
        ab_lines = has_numbers(line)
        if ab_lines == False:
            sample_line = line.strip().lower()
            samples.append(sample_line)
        else:
            pass
        
    return samples

def has_numbers(line): # helper function to not get digits
    return any(char.isdigit() for char in line)

def create_samples(sampled_lines, nr_of_samples):
    randomized_content = random.sample(sampled_lines, k=nr_of_samples)
    new_samples = []
    for line in randomized_content:
         for i in range(len(line)-5):
                print(i)
                
    return randomized_content
    

    
    
    
if __name__ == "__main__":
    sampled_lines = sample_lines("/scratch/UN-english.txt.gz")
    get_samples = create_samples(sampled_lines, 50)
    print(get_samples)
