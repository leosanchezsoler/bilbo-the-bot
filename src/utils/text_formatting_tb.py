import re # import regex
from nltk.corpus import stopwords
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer

def get_names(col):
    '''
    @leosanchezsoler
    This function is thought to get names when a cell in a dataframe is an HTML dict
    Parameters:
        - col: a column of a DataFrame
    Returns:
        - col: the column with the right format
    '''
    if isinstance(col, list):
        names = [i['name'] for i in col]
        #Check if more than 3 elements exist. If yes, return only first three. If no, return entire list.
        if len(names) > 3:
            names = names[:3]
        return names

def get_link(col):
    '''
    @leosanchezsoler
    This function is thought to get links when a cell in a dataframe is an HTML dict
    Parameters:
        - col: a column of a DataFrame
    Returns:
        - col: the column with the right format
    '''
    for i in col:
        return i['href']
    
def get_tag(col):
    '''
    @leosanchezsoler
    This function is thought to get links when a cell in a dataframe is an HTML dict
    Parameters:
        - col: a column of a DataFrame
    Returns:
        - col: the column with the right format
    '''
    if isinstance(col, list):
        terms = [i['term'] for i in col]
        #Check if more than 5 elements exist. If yes, return only first five. If no, return entire list.
        if len(terms) > 5:
            terms = terms[:5]
        return terms


def clean_text(text):
    '''
    @leosanchezsoler
    This function removes all items in a text except the alphabet
    Parameters:
        - text: the feature that will be formatted
    Returns:
        - text: a cleaned text 
    '''
    # remove everything except alphabets
    text = re.sub("[^a-zA-Z]", " ", text)
    # remove whitespaces
    text = ' '.join(text.split())
    text = text.lower()
    
    return text

def apply_clean_text(df, cols):
    '''
    @leosanchezsoler
    This function creates new columns with formatted text.
    Parameters:
        - cols: a list of columns which will be formatted
    '''
    for col in cols:
        df['clean_' + col] = df[col].apply(clean_text)
    return f'{cols} have been cleaned and formatted'

def remove_stop_words(text):
    '''
    This function returns a text without stopwords
    Parameters:
        - text: a string
    Returns:
        - no_stopword_text: a string from text after removing stopwords
    '''
    # Create a set of the stopwords
    stop_words = set(stopwords.words('english'))

    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)

def create_embedding_matrix(vocab_size):
    '''
    @leosanchezsoler
    This function is used to create the necessary embedding matrix that will be used for training the model
    Parameters:
        - vocab_size: an integer with the length of the vocabulary
    '''
    tokenizer = Tokenizer()
    embedding_matrix = np.zeros((vocab_size, 300))
    for word, i in  tokenizer.word_index.items():
            embedding_vector = word_vectors[word]
            embedding_matrix[i] = embedding_vector
    return embedding_matrix


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
