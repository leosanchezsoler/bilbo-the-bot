import pandas as pd 
import numpy as np 
import nltk
import json

def save_freq_words(df, col, terms = 30):
    '''
    @leosanchezsoler
    This function is made to save the most repeated words in a dataset in order to plot them in a wordcloud
    Parameters:
        - df: a pandas DataFrame
        - col: the desired column
        - terms: 

    '''
    all_words = ' '.join([text for text in df[col]])
    all_words = all_words.split()
    
    freq_dist = nltk.FreqDist(all_words)
    words_df = pd.DataFrame({'word':list(freq_dist.keys()), 'count':list(freq_dist.values())})
    words_df.sort_values(by='count', ascending=False, inplace=True)
    words_df.to_json('data/wordcloud.json', indent=4, orient='records')