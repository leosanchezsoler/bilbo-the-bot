import transformers

MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
ACCUMULATION = 2
BERT_PATH = 
MODEL_PATH = '../models/model.h5'
TRAINING_FILE = '..data/data.json'
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    'BERT_PATH',
    do_lower_case = True)