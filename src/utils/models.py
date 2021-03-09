from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support as score

def get_performance(y_test, y_pred):
    '''
    @leosanchezsoler
    This function returns metrics of the applied machine learning model
    Parameters:
        - y_test: a test set
        - y_pred: a prediction set
    Returns:
        - accuracy
        - precision
        - recall
        - f1score
    '''
    # Evaluate Performance
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
    # Get precision, recall, f1 scores
    precision, recall, f1score, support = score(y_test, y_pred, average='micro')

     # Performance metrics
    print(f'Test Accuracy Score of Basic Log. Reg.: % {accuracy}')
    print(f'Precision : {precision}')
    print(f'Recall    : {recall}')
    print(f'F1-score   : {f1score}')
    return accuracy, precision, recall, f1score