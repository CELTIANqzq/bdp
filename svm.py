import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import  pandas  as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score#R square
df=pd.read_csv('Dataset/简洁.csv') #这个会直接默认读取到这个Excel的第一个表单
pd.set_option('display.max_columns',None) #设置显示列数
pd.set_option('display.max_rows',None) #设置显示行数
data=df.head()

book_data = np.zeros([0,2], dtype = int)
count=0;
for line in df.itertuples():
    book_data=np.insert(book_data,count, [[line.num_pages,line.year]], axis=0)
    count=count+1
book_target=np.array(df.average_rating)
X_train,X_test,y_train,y_test= train_test_split(book_data,book_target,train_size=0.9,test_size=0.1,random_state=0)

#选用不同的核函数，第三种最好
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# clf_1 = SVR(kernel='linear')
# clf_1.fit(X_train, y_train)
# y_pred_1 = clf_1.predict(X_test)
# print(y_pred_1)
# print('MSE为：',mean_squared_error(y_test,y_pred_1))

# clf_2 = SVR(kernel='poly')
# clf_2.fit(X_train, y_train)
# y_pred_2 = clf_2.predict(X_test)
# print(y_pred_2)
# print('MSE为：',mean_squared_error(y_test,y_pred_2))


# clf_3 = SVR(kernel='rbf')
# clf_3.fit(X_train, y_train)
# y_pred_3 = clf_3.predict(X_test)
# score=clf_3.score(X_test,y_test)
# print(y_test)
# print(y_pred_3)
# print('MSE为：',mean_squared_error(y_test,y_pred_3))
# print('R Squared为：',r2_score(y_test,y_pred_3))

#线性回归
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
print(y_test)
print(y_pred)
print('MSE为：',mean_squared_error(y_test,y_pred))
print('R Squared为：',r2_score(y_test,y_pred))