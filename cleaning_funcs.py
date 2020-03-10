import re


r_clean_special_chars = re.compile(r'[^\w,.?!]|_')
r_dedupe_spaces = re.compile(r'\s+')
r_remove_newlines = re.compile(r'\n+')
r_remove_empty_sentences = re.compile(r'([.!?])\W+[.!?]')
r_sentence_boundary = re.compile(r'\s?[.!?]\s?')
r_remove_digits = re.compile(r'\d+')


def remove_boundaries(text):
    return r_sentence_boundary.sub('', text)


def clean_special_chars(text):
    return r_clean_special_chars.sub(' ', text)


def dedupe_spaces(text):
    return r_dedupe_spaces.sub(' ', text)


def remove_newlines(text):
    return r_remove_newlines.sub('', text)


def remove_empty_sentences(text):
    return r_remove_empty_sentences.sub('\\1', text)


def split_sentences(text):
    return r_sentence_boundary.split(text)[:-1]


def remove_digits(text):
    return r_remove_digits.sub('', text)


def tup_list_maker(tup_list):
    """
    Takes a list of tuples with index 0 being the text_id and index 1 being a 
    list of sentences and broadcasts the text_id to each sentence
    """
    final_list = []
    for item in tup_list:
        index = item[0]
        sentences = item[1]
        for sentence in sentences:
            pair = (index, sentence)
            final_list.append(pair)
    return final_list


def is_summary(number):
    """
    Takes a number as input
    Identifies a sentence as part of the summery or not
    """
    if number != 0:
        return 'yes'
    else:
        return 'no'


def is_sentence(sentence):
    """
    Evaluates if the input is a sentence (more than one word) 
    """
    return len(sentence.split(' ')) > 1


def clean_newline(sentence):
    """
    Deletes the '\n' character at the begining of some sentences
    """
    word_list = sentence.split(' ')
    first_word = word_list[0]
    if first_word[:1] == '\n':
        return sentence[1:]
    else:
        return sentence
