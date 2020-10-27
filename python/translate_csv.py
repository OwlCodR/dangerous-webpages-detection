from googletrans import Translator
import csv
import codecs

# This file translates dataset to some language

def translate_csv(dataset_path, dataset_delimiter, output_path, output_delimiter, lang_tag):
    with codecs.open(dataset_path, encoding='utf-8') as csv_file_en:
        with codecs.open(output_path, mode="w", encoding='utf-8') as csv_file_ru:
            translator = Translator()
            file_reader = csv.reader(csv_file_en, delimiter = ",")
            file_writer = csv.writer(csv_file_ru, delimiter = ",")
            count = 1
            for row in file_reader:
                if count != 0 and len(row[1]) != 0:
                    print([count, row[1]])
                    file_writer.writerow([count, translator.translate(row[1], dest='ru').text])
                count += 1

if __name__ == "__main__":
    dataset_path = "dataset/suicide_notes.csv"
    dataset_delimiter = ','

    output_path = "dataset/suicide_notes_translated.csv"
    output_delimiter = ','

    lang_tag = 'ru'

    translate_csv(dataset_path, dataset_delimiter, output_path, output_delimiter, lang_tag)