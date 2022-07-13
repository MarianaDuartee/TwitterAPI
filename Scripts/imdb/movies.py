import pandas as pd

def get_movies(p):
    df = pd.read_csv(p, sep='\t', low_memory=False)
    df['startYear'] = df['startYear'].replace(['\\N'],'0')
    df['startYear'] = df['startYear'].astype(int)
    dfMovies = df.loc[(df['titleType'] == 'movie') & (df['startYear'] >= 2012)]
    dfTitulos = dfMovies['tconst']

    del df
    del dfMovies

    return dfTitulos