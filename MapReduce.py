from datetime import datetime, date
import pandas as pd
import numpy as np


outputFile = r'year.csv'
def Map(fileName):
    df = pd.read_csv(fileName, sep=',',encoding='unicode_escape')
    publication_date=df['publication_date']
    average_rating=df['average_rating']
    bookID=df['bookID']
    for i in range(0,len(publication_date)):
        line = publication_date[i].split('/')
        year=line[2]
        with open(outputFile, 'a') as f:
            f.write(str(bookID[i])+','+str(year) + '\n')
Map('Dataset/月日年.csv')