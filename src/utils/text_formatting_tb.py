import re # import regex

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
