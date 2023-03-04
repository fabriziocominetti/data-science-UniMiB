import numpy as np
import pandas as pd
import re
import string
from tqdm import tqdm

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from multiprocessing import Pool


def remove_numbers(text_to_preprocess):
    return re.sub(r'\d+', '', text_to_preprocess)


def remove_punctuation(text):
    return text[0].translate(str.maketrans('', '', string.punctuation))


def remove_stopwords(text):
    no_stopwords = ''
    for item in text.split():
        if item not in stopwords.words():
            no_stopwords += ' '+item
    return no_stopwords


def postagger(token_words):
    return nltk.pos_tag(token_words)


def remove_extra_whitespace(text):
    return " ".join(text.split())


def tokenizer(text):
    return word_tokenize(text)


def lemmatizer_function(tokenized_text):
    lemmatized_text = ''
    for token in tokenized_text:
        lemmatized = lemmatizer.lemmatize(token)
        lemmatized_text += ' '+lemmatized
    return lemmatized_text


def preprocess_loader(dataframe):
    tqdm.pandas()
    dataframe['preprocessed_text'] = dataframe['text'].apply(preprocess_text)
    return dataframe


def preprocess_text(text):
    text = text.lower()
    no_nums = remove_numbers(text),
    no_punct = remove_punctuation(no_nums)
    no_stopw = remove_stopwords(no_punct)
    no_whtspace = remove_extra_whitespace(no_stopw)
    tokenized = tokenizer(no_whtspace)
    lemmatized = lemmatizer_function(tokenized)
    return lemmatized


lemmatizer = WordNetLemmatizer()

if __name__ == '__main__':
    train_ds = pd.read_csv('./data/train_dataset.csv')
    df_split = np.array_split(train_ds, 100000)
    pool = Pool(16)
    results = tqdm(pool.imap(preprocess_loader, df_split),
                   total=len(train_ds))
    df = pd.concat(results)
    pool.close()
    pool.join()
    df.to_csv('./train.csv')
