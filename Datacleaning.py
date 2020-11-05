import sys
from datetime import datetime
import re

def if_contain_symbol(keyword):
    if re.search(r"\W", keyword):
        return True
    else:
        return False

def map():
    count=0
    for line in sys.stdin:
        count=count+1
        if(count>1):
          data = line.strip().split()
          print(data)
          bookID = float(data[0])
          title = str(data[1])
          author = str(data[2])
          average_rating = float(data[3])
          isbn = float(data[4])
          isbn13=float(data[5])
          language_code=str(data[6])
          num_page=int(data[7])
          ratings_count=int(data[8])
          text_reviews_count=int(data[9])
          publication_date=datetime.strptime(data[10], '%Y-%m-%d')
          publisher=str(data[11])
          print(bookID)
          # if(average_rating>0 and average_rating<5 and if_contain_symbol(title)==False and if_contain_symbol(author)==False):
          #     print(bookID)
        #print("\t".join([key, value]))

if __name__ == "__main__":
    map()