import json
import os
import nltk


def read_config():
    with open('config.txt', 'r') as file:
        return json.load(file)


def download_nltk( nltk_folder : str ):
    nltk.download('averaged_perceptron_tagger', download_dir=nltk_folder)
    nltk.download('omw-1.4', download_dir=nltk_folder)
    nltk.data.path.append(nltk_folder)
    os.environ['NLTK_DATA'] = nltk_folder

