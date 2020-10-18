import csv
import codecs
from pymystem3 import Mystem
from openpyxl import load_workbook

wb = load_workbook('dataset/big_dataset.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
with codecs.open("dataset/big_dataset_lemma.csv", mode="w", encoding='utf-8') as csv_file_lemma:
    file_writer = csv.writer(csv_file_lemma, delimiter = "\t")
    m = Mystem()
    for i in range(1, 64040):
        lemmas = m.lemmatize(sheet.cell(row=i, column=1).value)
        string = ''.join(lemmas)
        print(string)
        file_writer.writerow([string, sheet.cell(row=i, column=2).value])