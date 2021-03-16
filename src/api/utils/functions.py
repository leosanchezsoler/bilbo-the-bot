import json
import pandas as pd
from nltk.stem import WordNetLemmatizer

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

def read_my_json():
    '''
    @leosanchezsoler
    This function reads the data
    Returns:
        - my_json
    '''
    df = pd.read_json('data/data.json')
    return df.to_json(orient='records', indent=4)


def tokenize_and_lemmatize(text):
    '''
    @leosanchezsoler
    This function transforms words in order to attach them to their root
    Parameters:
        - text
    Returns:
        - lem: the lemmatized text
    '''

    lemmatizer = WordNetLemmatizer()
    
    # tokenization to ensure that punctuation is caught as its own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    lem = [lemmatizer.lemmatize(t) for t in filtered_tokens]
    return lem