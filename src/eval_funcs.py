import pandas as pd
import numpy as np
import scipy
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
nlp = spacy.load("en_core_web_lg")


def feature_extractor(df):

    # Write a function that extracts features from new input
    wikihow = pd.read_csv('./datasets/wikihow_sep_features.csv')

    # Get sentence len
    df['sentence_len'] = df['sentence'].apply(lambda x: len(x.split(' ')))

    # Get tfidf scores
    tf_idf_list = []
    tfidf = TfidfVectorizer()
    tfidf.fit(wikihow['sentence'])
    vectors = tfidf.transform(df['sentence'])
    for vector in vectors:
        tfidf_sent = np.sum(vector)
        tf_idf_list.append(tfidf_sent)
    df['tfidf_score'] = tf_idf_list


def prediction_preprocessing(df):
    '''
    Call this function after fitting the text to the count vectorizer to create a
    sparse matrix of features to add to the BOW sparse matrix.
    '''

    # Reshaping the feature lengths array
    sent_lengths = np.array(df['sentence_len'].values).reshape(-1, 1)
    sent_tfidf = np.array(df['tfidf_score'].values).reshape(-1, 1)
    sent_title_sim = np.array(df['title_similarity'].values).reshape(-1, 1)

    # Converting features array to sparse matrix
    sparse_sent_lengths = scipy.sparse.csr_matrix(sent_lengths)
    sparse_sent_tfidf = scipy.sparse.csr_matrix(sent_tfidf)
    sparse_title_sim = scipy.sparse.csr_matrix(sent_title_sim)
    X_feats = scipy.sparse.hstack(
        [sparse_sent_lengths, sparse_sent_tfidf, sparse_title_sim])
    # Return a sparse matrix of extra features
    return X_feats

    # Get similarity to title


def get_similarity(term1, term2):
    sent1 = nlp(term1)
    sent2 = nlp(term2)
    return sent1.similarity(sent2)


# print(prediction_preprocessing(text, vectorizer))
def calculate_recall_distribution(df, predictions, y_test):
    df['predictions'] = predictions
    df['results'] = y_test

    df = df.sort_values(by='text_id')
    id_list = df['text_id'].unique()
    recalls = list()
    for identifier in id_list:

        temp_frame = df[df['text_id'] == identifier]
        recall = temp_frame[(temp_frame['results'] == 1) & (temp_frame['predictions'] == 1)]['text_id'].count(
        )/temp_frame[temp_frame['results'] == 1]['text_id'].count()

        recalls.append((identifier, recall))

    return recalls


def recreate_summaries(df, prediction='predictions', summary='is_summary', sentences='sentence'):
    real_summary = df[df[summary] == 1][sentences]
    real_summary.str.cat(sep='.')
    pred_summary = df[df[prediction] == 1][sentences]

    print(
        f"Real Summary: \n\n{real_summary.str.cat(sep='. ')} \n\nPredicted Summary: \n\n{pred_summary.str.cat(sep='. ')}")


def calculate_compression(df, prediction='predictions', summary='is_summary', sentences='sentence'):
    real_summary = df[df[summary] == 1][sentences].count()
    pred_summary = df[df[prediction] == 1][sentences].count()

    number_of_sentences = df[sentences].count()

    real_compression = real_summary/number_of_sentences
    pred_compression = pred_summary/number_of_sentences

    recall = df[(df[summary] == 1) & (df[prediction] == 1)][sentences].count(
    )/df[df[summary] == 1][sentences].count()

    result_df = pd.DataFrame()

    print(
        f"Real Compression: {real_compression} \n\nPredicted Compression: {pred_compression} \n\nRecall: {recall}")
