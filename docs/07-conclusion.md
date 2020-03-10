# Conclusion

After selecting a labeled dataset, preprocessing and extracting features from it, applying two different supervised techniques as well as one unsupervised techniques, selecting the proper performance metrics and finally comparing the performance of every one of them

We came to the conclusion that the best model in terms of precision-recall balance is the Multinomial Naive Bayes+LDA model.

This model can be improved using other preprocessing techniques like stemming and other feature extraction techniques such as sentence similarity (for both supervised and unsupervised techniques). We can also extract other types of features like part of speech tagging, Named entity recognition as well as verb concentration as a more advanced way to increase our model&#39;s performance.

Another approach could also be the use of [Hidden Markov Models](https://www.wikiwand.com/en/Hidden_Markov_model) or [Conditional Random Fields](https://www.wikiwand.com/en/Conditional_random_field) which have shown better performance than other techniques because they assume inter-sentence dependency.

Since the use of classifiers for text summarization requires a set of labeled documents and since the availability and diversity of such documents is currently limited, we can also use semi-supervised approaches to combine relatively small amounts of labeled data with a large amount of unlabeled data as a starting point for training.

[code for the project](https://github.com/sarisboo/springboard/tree/master/capstone_1)

[slides for the project](https://docs.google.com/presentation/d/1T3aWwdivKmzD7NSSghumf19eMmXwHnLz0Im-1saDYxw/edit?usp=sharing)