from scipy.stats import pearsonr
import  pandas  as pd
import numpy as np
df=pd.read_csv('Dataset/train_supplement.csv')#这个会直接默认读取到这个Excel的第一个表单
pd.set_option('display.max_columns',None) #设置显示列数
pd.set_option('display.max_rows',None) #设置显示行数
data=df.head()
#皮尔森相关系数判定是否线性相关，越接近1越有相关性
pccs_num_pages = pearsonr(df.num_pages, df.average_rating)
print(pccs_num_pages)
print("num_pages:"+str(pccs_num_pages))
pccs_ratings_count = pearsonr(df.ratings_count, df.average_rating)
print("ratings_count:"+str(pccs_ratings_count))
pccs_text_reviews_count = pearsonr(df.text_reviews_count, df.average_rating)
print("text_reviews_count:"+str(pccs_text_reviews_count))
#
#将三个数据值和一个评分分别转换为np.array模式
book_data = np.zeros([0,3], dtype = int)
count=0;
for line in df.itertuples():
    book_data=np.insert(book_data,count, [[line.num_pages, line.ratings_count, line.text_reviews_count]], axis=0)
    count=count+1
book_target=np.array(df.average_rating)
threshold=10000
np.set_printoptions(threshold=np.inf)
# print(book_data)
# print(book_target.shape)


#用互信息和最大信息系数 (Mutual information and maximal information coefficient (MIC) 得出相关系数最大的是属性num_pages
from minepy import MINE
from numpy import array
from sklearn.feature_selection import SelectKBest
def mic(x, y):
    m = MINE()
    m.compute_score(x, y)
    return (m.mic(), 0.5)
book_data_new =  SelectKBest(lambda X, Y: tuple(map(tuple,array(list(map(lambda x:mic(x, Y), X.T))).T)), k=1).fit_transform(book_data, book_target)
# print(book_data_new)
print(book_data_new.shape)
