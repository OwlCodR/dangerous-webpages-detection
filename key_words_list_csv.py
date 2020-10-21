import csv
import codecs
import string

dictionary = {}

with codecs.open("dataset/big_dataset_lemma.csv", encoding='utf-8') as csv_file_dataset:
    file_reader = csv.reader(csv_file_dataset, delimiter = " ")
    count = 1
    for row in file_reader:
        if row[1] == '1.0':
            for word in row[0].rstrip(string.punctuation).split():
                if dictionary.get(word) == None:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
            count += 1
dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

with codecs.open("dataset/big_dataset_lemma_key_words.csv", mode="w", encoding='utf-8') as csv_file_key_words:
    file_writer = csv.writer(csv_file_key_words, delimiter = "\t")
    for i in dictionary:
        file_writer.writerow([i, dictionary[i]])
