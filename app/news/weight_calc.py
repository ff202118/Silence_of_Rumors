# -*- coding: utf-8' -*-
import tagme
import pandas as pd
import pickle as pkl

tagme.GCUBE_TOKEN = "813a5b09-e661-4799-9344-67bec90a72f9-843339462"

corpus = []
df = pd.read_excel('Data.xlsx')
for cnt in range(10):
    corpus.append(df.loc[cnt, 'content'])  # 获取 'content' 列的数据

def get(text):
    try:
        annotations = tagme.annotate(text)

        entity = set()

        for annotation in annotations.get_annotations(0.3):
            entity_title = annotation.entity_title
            entity.add(entity_title)

        return list(entity)
    except TimeoutError:
        print("Function timed out")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

from tqdm import tqdm

entity = []
for text in tqdm(corpus):
    entity.append(get(text))

print(entity)