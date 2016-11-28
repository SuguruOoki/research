# coding:utf-8

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
 
np.set_printoptions(precision=2)
 
docs = np.array([
        '白 黒 赤',      # 文書１
        '白 白 黒',      # 文書２
        '白 黒 黒 黒',   # 文書３
        '白'            # 文書４
        ])
 
vectorizer = TfidfVectorizer(input=u'../corpus/' use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
print vectorizer.fit_transform(docs).toarray()