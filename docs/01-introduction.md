# Introduction

## Problem

Every day, we are flooded with information from our phones and computers. This kind of information overload is one of the main causes of digital stress which in turn leads to productivity loss.

A big part of the information overload problem is the almost infinite amount of resources we can find on the internet, this can make the process of selecting useful information quite tedious: usually we comb through every single article and patch up information here and there which takes up a lot of time and energy.

## Approach

There are basically two main ways to perform text summarization.

- **Extractive methods** : identifies important sections of the text and produces a subset of sentences from the original text.
- **Abstractive methods** : reproduces the important material in a new way after interpretation and examination of the text and generates a much shorter text that only conveys critical information. It is closer to human interpretation than the first method.

In this project, we will focus on exploring and evaluating different approaches to text summarization using extractive techniques.

## Literature review

There are various [extractive techniques](https://medium.com/sciforce/towards-automatic-text-summarization-extractive-methods-e8439cd54715) for [summarization](https://arxiv.org/pdf/1707.02268.pdf), some are topic-based approaches using [topic signatures](https://www.aclweb.org/anthology/J93-1003/) in order to determine the importance of a sentence, others are based the on frequency of words and text semantics as importance indicators like  [TF-IDF](https://medium.com/voice-tech-podcast/automatic-extractive-text-summarization-using-tfidf-3fc9a7b26f5) and [LSA](http://lsa.colorado.edu/papers/JASIS.lsi.90.pdf)  and we also have  graph methods that combine inter-sentence similarity and TF-IDF  to create a graph representation of the documents. Another approach is to treat summarization as a classification problem and try to apply different machine learning algorithms to obtain a reliable summary.