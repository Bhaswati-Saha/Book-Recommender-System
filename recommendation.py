import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


final_rating=pd.read_csv('models/Final_Rating.csv')
book_pivot=final_rating.pivot_table(columns='user_id',index='title',values='rating')
book_pivot.fillna(0,inplace=True)
book_sparse=csr_matrix(book_pivot)
model=NearestNeighbors(algorithm='brute')
model.fit(book_sparse)

def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    x = []

    for j in book_pivot.index[suggestions[0]]:
            x.append(j)
    y=[]
    for i in range(1, len(x)):
        y.append(x[i])
    return y