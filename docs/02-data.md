# 📚 Data

For this analysis, we will use the [wikihow](https://www.tensorflow.org/datasets/catalog/wikihow) dataset. In a wikihow article structure, every paragraph starts with a sentence that summarizes what the whole paragraph will be about.This type of summary is exactly what we need when we use an extractive method for text summarization.

## Raw Data

In the wikihow dataset, we count 1585695 observations collected with the following features:

* **headline** : Consists of sentences summarizing the contents for each paragraph in each wikihow article.
* **text** : Contents of each paragraph for that specific headline for that specific article.
* **sectionLabel** : What type of section, for example is it a title or a step. The top label here is `steps` since the articles are a majority of &#39;how to&#39; articles.
* **title** : title of the article.

## Extracted Features

From this raw data we extracted the following features:

* **sentence** : We split the **text** column into sentences.
* **is_summary** : For each of these sentences, we assign 1 if it is a summary (headline) sentence, 0 otherwise.
* **text_id** : Useful column to track the provenance of each sentence (which article it  belongs to).
* **sentence_len** : Length of each sentence as in number of words.
* **tfidf_score** : Sentence tf idf score (Using sklearn&#39;s tfidf vectorizer on each word and computing the sum of tfidf for each sentence, stopwords were previously removed)
* **title_similarity** : For each sentence, we compute its similarity score to the title (using spacy which uses cosine similarity to compute it).

[**Next: 🎯 Project Aims**](03-project-aims.md)