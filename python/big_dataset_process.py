from googletrans import Translator
from pymystem3 import Mystem
from openpyxl import load_workbook
import csv
import urllib
import string
import re
import codecs

# This file processing big .xlsx dataset
# Debug version

def get_sentences(text):
    print('get_sentences')
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.split('.')
    text = [x for x in text if len(x) > 1]
    return text

def get_removed_punctuation(sentences):
    print('get_removed_punctuation')

    for i in range(len(sentences)):
        sentences[i] = sentences[i].lower()
        sentences[i] = ' '.join(re.findall(r'[А-я]+', sentences[i]))
    sentences = [x for x in sentences if len(x) > 1]
    return sentences

def get_translated_sentences(sentences):
    print('get_translated_sentences')

    translator = Translator()

    for i in range(len(sentences)):
        sentences[i] = translator.translate(sentences[i], dest='ru').text
        print(sentences[i])

    return sentences

def get_lemmatize_sentences(sentences, mystem):
    print('get_lemmatize_sentences')

    for i in range(len(sentences)):
        lemmas = mystem.lemmatize(sentences[i])
        sentences[i] = ''.join(lemmas).replace('\n', '')
        print([sentences[i]])

    return sentences

def get_contained_key_words(key_words_path, output_delimiter, sentences, key_words):
    print('get_contained_key_words')

    for sentence in sentences:
        isKeyWord = False
        for key_word in key_words[:1113]:
            if key_word in sentence:
                isKeyWord = True
                #print('isKeyWord -> ', key_word)
                break
        if not isKeyWord:
            sentences.remove(sentence)
            #print('Removed -> ', sentence)
    return sentences
                

if __name__ == "__main__":
    lemma_text_count = 4

    dataset_path = "python/server/dataset/big_dataset.xlsx"

    key_words_path = "python/server/dataset/key_words2.csv"
    key_words_delimiter = '\t'

    output_path = "python/server/dataset/big_dataset.csv"
    output_delimiter = '\t'

    wb = load_workbook(dataset_path)
    sheet = wb.get_sheet_by_name('Sheet1')

    with open(output_path, mode="w", encoding='utf-8') as output:
        with open(key_words_path, encoding='utf-8') as key_words_csv:
            file_reader = csv.reader(key_words_csv, delimiter = output_delimiter)
            file_writer = csv.writer(output, delimiter = output_delimiter)
            mystem = Mystem()

            key_words = []
            for row in file_reader:
                key_words.append(row[0])

            for i in range(1, lemma_text_count):
                dataset_text = sheet.cell(row=i, column=1).value
                dataset_markup = sheet.cell(row=i, column=2).value

                print(dataset_text)
                sentences = get_sentences(dataset_text)
                print(sentences)
                sentences = get_translated_sentences(sentences)
                print(sentences)
                sentences = get_removed_punctuation(sentences)
                print(sentences)
                sentences = get_lemmatize_sentences(sentences, mystem)
                print(sentences)
                sentences = get_contained_key_words(key_words_path, key_words_delimiter, sentences, key_words)
                print(sentences)
                for sentence in sentences:
                    file_writer.writerow([sentence, dataset_markup])