import os, sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

import pandas as pd 
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from api.utils.functions import tokenize_and_lemmatize


def get_recommendations(title, df, tfidf_vect):
    '''
    @leosanchezsoler
    This function recommends articles based on cosin similarity
    Parameters:
        - title: A string with the user input
        - similarity: the measure employed for the recommendation engine
    
    Returns:
        - df[['link', 'title']].iloc[article_indices]
    ''' 
    try:
        idx = df.index[df['title'] == title]
    
    except:
        'Article not found. Please make sure it is one of the titles in arxivData'
    
    
    # pairwise similarity scores
    
    show_cos_sim = cosine_similarity(tfidf_vect[idx, tfidf_vect])

    sim_titles_vect = sorted(list(enumerate(show_cos_sim)), key=lambda x: x[1], reverse=True)[1:11]
    # sorting


    article_indices = [i[0] for i in show_cos_sim]
    result = df[['link', 'title']].iloc[article_indices]
    # Return the top 10 most related articles
    return result


def new_one(title, df, similarity):
    idx = df.index[df['title'] == title]
    # pairwsie similarity scores
    sim_scores = list(enumerate(similarity[idx]))
    # sorting
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    article_indices = [i[0] for i in sim_scores]
    # Return the top 10 most related articles
    return df[['link', 'title']].iloc[article_indices]