from http.server import BaseHTTPRequestHandler, HTTPServer
from googletrans import Translator
import pymorphy2
import urllib
import string
import re
import codecs
import csv
import auto_request 

from MLib import ML

# This file started simple python server
# And it handles requests from addons

morph = pymorphy2.MorphAnalyzer(lang='ru')
translator = Translator()
ml = ML()
ml.load_all_clf()


def get_mathces_percent(sentences):
    match_count = 0.0
    words_count = 0.0
    with open("dataset/key_words.csv", encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter = '\t')
        for sentence in sentences:
            words_count += len(sentence.split())
            for row in file_reader:
                if row[0] in sentence:
                    match_count += 1
            print(match_count)
            print(words_count)
    return match_count / words_count


def get_result(sentences):
    print('get_result')
    percent = sum(ml.svc.predict(sentences)) / len(sentences) * 100
    print(percent)

    #percent = get_mathces_percent(sentences)
    #percent = 12
    # Machine Learning Here

    if percent > 30:
        #return 'block'
        return percent
    else:
        #return 'ok'
        return percent


def get_sentences(text):
    print('get_sentences')
    if type(text) == bin:
        text = text.decode()
    text = text.replace('text=', '')
    text = urllib.parse.unquote_plus(text)
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')
    text = text.split('.')
    text = [x for x in text if len(x) > 1]
    return text


def get_removed_punctuation(sentences):
    print('get_removed_punctuation')

    for i in range(len(sentences)):
        sentences[i] = sentences[i].lower()
        sentences[i] = ' '.join(re.findall(r'[А-я]+', sentences[i]))
        sentences[i] = ' '.join([word for word in sentences[i].split() if morph.parse(word)[0].tag.POS not in ['PREP', 'CONJ', 'PRCL', 'INTJ', 'NUMR'] or word == 'не' or word == 'ни'])
    sentences = [x for x in sentences if len(x) > 1]
    #print(sentences)
    return sentences


def get_translated_sentences(sentences):
    print('get_translated_sentences')

    for i in range(len(sentences)):
        if len(sentences[i]) > 0:
            sentences[i] = translator.translate(sentences[i], dest='ru').text
        #print(sentences[i])

    return sentences


def get_lemmatize_sentences(sentences):
    print('get_lemmatize_sentences')

    for i in range(len(sentences)):
        sentences[i] = ' '.join([morph.parse(word)[0].normal_form for word in sentences[i].split()])
        #print([sentences[i]])

    return sentences


def get_clear_sentences(text):

    # Main cleaning function

    # Splitting text into sentences
    # Translate sentences
    # Lowercase, remove punctuation and numbers
    # Lemmatize sentences

    # text example: спросить почему умереть ответить устать 

    print('get_clear_sentences')
    sentences = get_sentences(text)
    #print(sentences)
    #sentences = get_translated_sentences(sentences)
    #print(sentences)
    sentences = get_removed_punctuation(sentences)
    #print(sentences)
    sentences = get_lemmatize_sentences(sentences)
    #print(sentences)
    return sentences


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_GET(self):
        self._set_headers()
        self.wfile.write("received get request".encode())


    def do_POST(self):
        self._set_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(self.headers)
        self.wfile.write(get_result(get_clear_sentences(post_body)).encode())


def auto_requests():
    norm_soups = auto_request.get_normal_websites_soup()
    suicicde_soups = auto_request.get_suicide_contents_soup()

    true_suicide_count = 0
    true_normal_count = 0

    for norm_soup in norm_soups:
        print("NOW --> ", norm_soup.title)
        result = get_result(get_clear_sentences(norm_soup.get_text()))

        if result < 10:
            true_suicide_count += 1
            print("CORRECT NORM RESULT --> ", norm_soup.title, result)
        else:
            print("INCORRECT NORM RESULT --> ", norm_soup.title, result)
            #print(norm_soup.get_text())
            

    for suicicde_soup in suicicde_soups:
        print("NOW --> ", suicicde_soup.title)

        result = get_result(get_clear_sentences(suicicde_soup.get_text()))
        if result > 10:
            true_normal_count += 1
            print("CORRECT SUICIDE RESULT --> ", suicicde_soup.title, result)
        else:
            print("INCORRECT SUICIDE RESULT --> ", suicicde_soup.title, result)
            #print(suicicde_soup.get_text())
            
    # (10%) (50%)
    # NB (0.88 & 0.12) (0.92 & 0.84)
    # LSVC (0.92 & 0.28) (0.92 & 1)
    # SGD (0.92 & 0.72) (0.88 & 1)
    # SVC (0.96 & 0.44) (0.84 & 1)

    print('ИТОГИ')
    print('% NORMAL CORRECT = ', true_normal_count, true_normal_count / 25)
    print('% SUICIDE CORRECT = ', true_suicide_count, true_suicide_count / 25)

def run(server_class=HTTPServer, handler_class=HandleRequests, port=8080):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...\n')
    auto_requests()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping server...\n')


if __name__ == '__main__':
    run()