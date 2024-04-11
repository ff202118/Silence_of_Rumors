# -*- coding: utf-8 -*-
import jieba
import re

def clean_str(string):
    stop_words = []
    with open('哈工大停用词表.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)

    # print(string)

    res = jieba.lcut(string)
    clean_res = []
    for item in res:
        if item not in stop_words:
            clean_res.append(item)
    clean_res = ' '.join(clean_res)
    # print(clean_res)
    return clean_res