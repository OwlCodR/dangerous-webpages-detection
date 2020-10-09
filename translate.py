from googletrans import Translator
import csv
import codecs

with codecs.open("dataset/suicide_notes.csv", encoding='utf-8') as csv_file_en:
    with codecs.open("dataset/suicide_notes_translated.csv", mode="w", encoding='utf-8') as csv_file_ru:
        translator = Translator()
        file_reader = csv.reader(csv_file_en, delimiter = ",")
        file_writer = csv.writer(csv_file_ru, delimiter = ",")
        count = 1
        for row in file_reader:
            if count != 0 and len(row[1]) != 0:
                print([count, row[1]])
                file_writer.writerow([count, translator.translate(row[1], dest='ru').text])
            count += 1

