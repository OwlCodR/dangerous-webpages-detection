import csv
import codecs
import string

# This file generates a .csv file of most popular words in dataset
# First column - Word
# Second column - Number of occurrence

def generate_csv(dataset_path, dataset_delimiter, output_path, output_delimiter):
    dictionary = {}

    with codecs.open(dataset_path, encoding='utf-8') as csv_file_dataset:
        file_reader = csv.reader(csv_file_dataset, delimiter = dataset_delimiter)
        count = 1
        for row in file_reader:
            if row[1] == '1.0':
                words = row[0].rstrip(string.punctuation).split()
                for i in range(len(words)):
                    #print(words[i])
                    if 'не' == words[i] or 'ни' == words[i] or 'раз' == words[i]:
                        continue
                    if i - 1 > 0:
                        if 'не' == words[i - 1] or 'ни' == words[i - 1]:
                            words[i] = words[i - 1] + ' ' + words[i] 
                            print(words[i])   
                    if dictionary.get(words[i]) == None:
                        dictionary[words[i]] = 1
                    else:
                        dictionary[words[i]] += 1
                count += 1

    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

    with codecs.open(output_path, mode="w", encoding='utf-8') as csv_file_key_words:
        file_writer = csv.writer(csv_file_key_words, delimiter = output_delimiter)
        for i in dictionary:
            file_writer.writerow([i, dictionary[i]])

if __name__ == "__main__":

    dataset_path = "python/server/dataset/small_dataset.csv"
    dataset_delimiter = '\t'

    output_path = "python/server/dataset/key_words2.csv"
    output_delimiter = '\t'

    generate_csv(dataset_path, dataset_delimiter, output_path, output_delimiter)