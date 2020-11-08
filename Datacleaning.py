import  pandas  as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Train_test.csv')#这个会直接默认读取到这个Excel的第一个表单
pd.set_option('display.max_columns',None) #设置显示列数
pd.set_option('display.max_rows',None) #设置显示行数
def if_contain_symbol(keyword):
    if re.search(r"\W", keyword):
        return True
    else:
        return False
#判断评分在不在0-5之间
# for row in df.itertuples():
#   if(row.average_rating>0 and row.average_rating<5):
#      print(row.bookID)

# 检测乱码 //to do
for row in df.itertuples():
  # if(if_contain_symbol(row.title)==False):
  res=row.title
  res = res.encode('utf-8').decode('latin-1')
  print(res)
# df.to_csv("out.csv", index_label = "index")
# for line in df.bookID:
#    print(line)