import  pandas  as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
df=pd.read_csv('Dataset/简洁.csv')#这个会直接默认读取到这个Excel的第一个表单
pd.set_option('display.max_columns',None) #设置显示列数
pd.set_option('display.max_rows',None) #设置显示行数
data=df.head()


# vectorizer = CountVectorizer() # 先使用频率表示法
# transformer = TfidfTransformer() # 再使用tdif进行逆文档频率转换
# tfidf = transformer.fit_transform(vectorizer.fit_transform(df.title))
# print(tfidf.toarray()) # 输出数值化之后的矩阵

#太离散了
from sklearn.feature_extraction.text import TfidfVectorizer
# method2 直接使用TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=200)
X = vectorizer.fit_transform(df.title) # 拟合并且转化文本
print(vectorizer.get_feature_names()) # 输出特征字典
print(X.shape) # 输出文本的维数，
# print(X.toarray())
# for line in X.toarray():
#      print(line)