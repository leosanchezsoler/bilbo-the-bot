import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px 
import pandas as pd 

import tensorflow as tf


def freq_words(df, terms = 30, save=None, filename=None):
    '''
    @leosanchezsoler
    This function creates 2 graphs:
        1. A wordcloud with a specific amount of words
        2. A barplot displaying word frequencies
    
    Parameters:
        - df: a pandas Dataframe
        - terms: an integer indicating the amount of words that will be plotted
        - save: None by default. If true, the plot will be saved
        - filename: a string containing the name of the file
    '''
    all_words = ' '.join([text for text in df])
    all_words = all_words.split()
    
    freq_dist = nltk.FreqDist(all_words)
    words_df = pd.DataFrame({'word':list(freq_dist.keys()), 'count':list(freq_dist.values())})
    
    fig = plt.figure(figsize=(21,16))
    ax1 = fig.add_subplot(2,1,1)
    wordcloud = WordCloud(width=1000, height=300, background_color='black', 
                          max_words=1628, relative_scaling=1,
                          normalize_plurals=False).generate_from_frequencies(freq_dist)
    
    ax1.imshow(wordcloud, interpolation="bilinear")
    ax1.axis('off')
    
    ax2 = fig.add_subplot(2,1,2)
    d = words_df.nlargest(columns="count", n = terms) 
    ax2 = sns.barplot(data=d, palette = sns.color_palette('BuGn_r'), x= "count", y = "word")
    ax2.set(ylabel= 'Word')
    
    if save: 
        path_png = 'documentation/images/static/' + filename + '.png'
        plt.savefig(fname = path_png)
    
    plt.show()
    
def freq_tags(df, sort_by, x, y, n=20, save=None, filename=None):
    '''
    @leosanchezsoler
    This function is thought to plot the most frequent tags of a dataset in order to see the most relevant ones
    Parameters:
        - df: a pandas DataFrame
        - tags: a Dataframe column
        - n: the number of words to be considered
        - sort_by: a DataFrame column
        - x: the value that will be plotted in the x axis
        - y: the value that will be plotted in the y axis
        - save: if True, saves the file in png format
        - filename: the name of the file that will be saved
    '''
    graph = df.nlargest(columns=sort_by, n=n)
    plt.figure(figsize=(12,15))
    ax = sns.barplot(data=graph, x=x, y=y)
    ax.set(ylabel=y)
    ax.set(xlabel=x)
    
    if save:
        path_png = 'documentation/images/static/' + filename + '.png'
        plt.savefig(fname = path_png)
    
    plt.show()

def plot_sentence_distribution(X, save=None, filename=None):
    '''
    @leosanchezsoler
    This function plots distribution of sentences once they are tokenized
    Parameters:
        - X: input data
        - save: if True, saves the file in png format
        - filename: the name of the file that will be saved
    '''
    plt.hist([len(x) for x in X], bins=100)
    plt.figure(figsize=(12,15))

    if save:
        path_png = 'documentation/images/static/' + filename + '.png'
        plt.savefig(fname = path_png)
        
    plt.show()

def train_val_accuracy(model, filename=None, save=None):
    '''
    @leosanchezsoler
    This function shows the loss over epochs of a model
    Parameters:
        - Model: a tensorflow model
        - filename: a string containing the name of the plot
        - save: if True, the model is saved to png
    '''
    plt.plot(model.history['acc'], label='(data)')
    plt.plot(model.history['val_acc'], label='(validation data)')
    plt.title('Accuracy for Text Classification')
    plt.figure(figsize=(12,15))

    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    if save:
        path_png = 'documentation/images/static/' + filename + '.png'
        plt.savefig(fname = path_png)
        
    plt.show()

def model_loss(model, save=None, filename=None):
    '''
    @leosanchezsoler
    This function shows model loss over epochs
    Parameters:
        - model: a tensorflow model
    '''
    plt.plot(model.history['loss'])
    plt.plot(model.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(['train', 'val'])

    if save:
        path_png = 'documentation/images/static/' + filename + '.png'
        plt.savefig(fname = path_png)
        
    plt.show()
