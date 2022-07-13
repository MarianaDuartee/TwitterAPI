import pandas as pd


def get_actors_names(p,actors):
    df = pd.read_csv(p,sep='\t', low_memory=False)
    dfNames =  pd.merge(actors, df, on="nconst")
    dfTopActors = dfNames[['nconst', 'qtdMovies', 'primaryName']]
    dfTopActors = dfTopActors.head(10)
    lista = dfTopActors.values.tolist()

    del df
    del dfNames
    del dfTopActors

    return lista