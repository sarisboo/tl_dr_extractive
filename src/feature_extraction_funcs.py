import spacy
import pandas as pd
import numpy as np
nlp = spacy.load("en_core_web_lg")


def remove_last_element(lst):
    '''
    Removes first element in a list and
    appends it to the end of the list
    '''
    item = lst[0]
    lst[:] = lst[1:] + list(item)
    return lst


def similarity_calculator(document):
    similarities = list()
    for update in range(len(document)):
        updated_list = remove_last_element(document)
        elements = list()
        for sentence in updated_list[1:]:
            elements.append(nlp(updated_list[0]).similarity(nlp(sentence)))
        mean = sum(elements)/len(elements)
        similarities.append(mean)
    return similarities


#wikihow = pd.read_csv('./datasets/wikihow_features_v1.csv')
# Grouping dataframe by text_id
#docs = wikihow.groupby('text_id')['sentence'].apply(list)

# Generate similarity matrices
#docs_subset_1 = docs.iloc[:1]
#similarities_mat = docs_subset_1.apply(similarity_calculator)

# Checking similarity matrices
# print(len(similarities_mat))
#print(len(similarities_mat) == len(docs_subset_1))

# Saving the similarity matrix to a csv file
#similarities_mat.to_csv('./datasets/wikihow_similarity_mat_1.csv', index=False)
