# -*- coding: utf-8' -*-
import tagme
import pandas as pd
import pickle as pkl
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import clean_str

def get_ww(s):
    corpus = []
    df = pd.read_excel(f'{s}.xlsx')
    string = str()
    lens = len(df) if len(df) < 1000 else 1000
    for cnt in range(lens):
        string += df.loc[cnt, 'content']  # 获取 'content' 列的数据

    string = clean_str(string)
    corpus.append(string)


    def tfidf_keywords_with_weights(corpus, num_keywords=100):
        # 初始化TF-IDF向量化器
        vectorizer = TfidfVectorizer()

        # 将corpus中的文本转换为TF-IDF矩阵
        tfidf_matrix = vectorizer.fit_transform(corpus)

        # 获取所有特征词
        feature_names = vectorizer.get_feature_names_out()

        # 计算每个文本中词语的TF-IDF值及对应权重
        doc_keywords = []
        for doc_index in range(len(corpus)):
            doc_vector = tfidf_matrix[doc_index]
            sorted_indices = doc_vector.toarray().argsort()[0][-num_keywords:][::-1]
            doc_keywords_weights = [(feature_names[index], doc_vector[0, index]) for index in sorted_indices]
            doc_keywords.append(doc_keywords_weights)

        return doc_keywords


    # 提取关键词及权重
    keywords_with_weights = tfidf_keywords_with_weights(corpus)
    for doc_index, doc_keywords_weights in enumerate(keywords_with_weights):
        print(f"Document {doc_index+1} keywords with weights:")
        for keyword, weight in doc_keywords_weights:
            print(f"{keyword}: {weight}")
        print()

    with open(f'word_weight_{s}.pkl', 'wb') as f:
        pkl.dump(keywords_with_weights, f)

if __name__ == '__main__':
    get_ww('rumor')
    get_ww('refute')