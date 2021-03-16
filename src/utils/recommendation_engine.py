from sklearn.metrics.pairwise import cosine_similarity

def recommend_articles(title, df, tfidf_vec):
    '''
    Recommends 10 articles based on the title
    Parameters:
        - title: a string with the title of the article
        - df: a pandas Dataframe with the article dataset
        - tfidf_vec: TF-IDF sparse matrix
    
    Returns:
        - response: Recommended article links on a DataFrame
    '''
    try:
        title_iloc = df.index[df['']]
    
    except:
        return 'Topic not found. Please make sure it is one of the titles in the dataset.'
    
