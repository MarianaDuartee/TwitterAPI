import csv
import pandas as pd 
from pathlib import Path

def save_names(list_names):
    fields = ['nconst', 'qtdMovies','name']
    with open(r"", "w",encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(fields)
        w.writerows(list_names)

def get_names():
    list_names = []
    with open(r"","r", encoding='utf-8') as file:
        table = csv.DictReader(file)
        for col in table:
            list_names.append(col['name'])
    return list_names

def save_tweets(dfTweets):
    dfTweets.to_csv(r"",index=False)

    del dfTweets
