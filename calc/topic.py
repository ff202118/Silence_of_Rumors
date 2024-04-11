import pandas as pd
from modelscope.pipelines import pipeline
import pandas

p = pipeline('text-classification', model='damo/nlp_domain_classification_chinese')

def get_top(s):
    df = pd.read_csv(f'{s}.xlsx')
    for ind in range(len(df)):
        content = df.loc[ind, 'content']
        print(p(content))

if __name__ == '__main__':
    get_top('rumor')