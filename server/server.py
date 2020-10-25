from http.server import BaseHTTPRequestHandler, HTTPServer
from googletrans import Translator
from pymystem3 import Mystem
import urllib
import string
import re
import codecs
import csv

# This file started simple python server
# And it handles requests from addons

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

    percent = get_mathces_percent(sentences)

    # Machine Learning Here

    if percent > 10:
        return 'block'
    else:
        return 'ok'

def get_removed_punctuation(sentences):
    print('get_removed_punctuation')

    for i in range(len(sentences)):
        sentences[i] = sentences[i].lower()
        sentences[i] = ' '.join(re.findall(r'[А-я]+', sentences[i]))
    sentences = [x for x in sentences if len(x) > 1]
    print(sentences)
    return sentences

def get_translated_sentences(sentences):
    print('get_translated_sentences')

    translator = Translator()

    for i in range(len(sentences)):
        sentences[i] = translator.translate(sentences[i], dest='ru').text
        print(sentences[i])

    return sentences

def get_lemmatize_sentences(sentences):
    print('get_lemmatize_sentences')

    mystem = Mystem()

    for i in range(len(sentences)):
        lemmas = mystem.lemmatize(sentences[i])
        sentences[i] = ''.join(lemmas).replace('\n', '')
        print([sentences[i]])

    return sentences


def get_sentences(text):
    print('get_sentences')
    text = text.decode()
    text = text.replace('text=', '')
    text = urllib.parse.unquote_plus(text)
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.split('.')
    text = [x for x in text if len(x) > 3]
    return text

def get_clear_sentences(text):

    # Main cleaning function

    # Splitting text into sentences
    # Translate sentences
    # Lowercase, remove punctuation and numbers
    # Lemmatize sentences

    # text example: спросить почему умереть ответить устать 

    print('get_clear_sentences')
    sentences = get_sentences(text)
    print(sentences)
    sentences = get_translated_sentences(sentences)
    print(sentences)
    sentences = get_removed_punctuation(sentences)
    print(sentences)
    #sentences = get_lemmatize_sentences(sentences)
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
        get_result(get_clear_sentences(post_body))
        self.wfile.write("ok".encode())

def run(server_class=HTTPServer, handler_class=HandleRequests, port=8080):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping server...\n')

if __name__ == '__main__':
    run()