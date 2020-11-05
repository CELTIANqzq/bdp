import  pandas  as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Train_data.csv')#这个会直接默认读取到这个Excel的第一个表单
pd.set_option('display.max_columns',None) #设置显示列数
pd.set_option('display.max_rows',None) #设置显示行数
data=df.head()
#print(format(data))#默认读取前5行的数据
print(df.describe())
# print(df.average_rating.dtypes)
fig = plt.figure(figsize=(1, 1))
price = fig.add_subplot(111)
plt.title("分数")
sns.distplot(df.average_rating.astype('float'),color="red")
plt.show()