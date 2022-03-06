from flask import Flask
from flask import request
import requests
import json
from source.utils import read_config, download_nltk
from nltk.stem import WordNetLemmatizer
import nltk
import os, sys

app = Flask(__name__)

config  = read_config()
download_nltk(config['nltk_path'])


@app.route('/')
def test():
    return config['nltk_path'] or 'Empty'


@app.route('/pos')
def pos_route():
    word = request.args.get('word', '')
    if not word:
        return ''
    result = nltk.pos_tag([word])[0][1]
    return result


@app.route('/normalize')
def normalize_route():
    lemmatizer = WordNetLemmatizer()
    print(request.get_json())
    tokens = request.get_json()['tokens']
    tokens = [ lemmatizer.lemmatize(item.lower()) for item in tokens ]
    return {"tokens" : tokens}


@app.route('/pos_list')
def pos_list_route():
    print(request.get_json())
    print("URL: ", config["lemmatizer_path"])
    response = requests.get(config["lemmatizer_path"], json=request.get_json())
    tokens = response.json()['tokens']
    print("Lemmatized tokens", tokens)
    pos_tags = nltk.pos_tag(tokens)
    print("Pos tags", pos_tags)

    return "Done"



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
