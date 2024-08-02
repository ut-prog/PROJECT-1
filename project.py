#Import Libraries

import pandas as pd
import numpy as np

#Import Dataset

df = pd.read_csv(r'https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')


df.head()
df.info()
df.shape
df.columns

#Get Feature Selection

df_features = df[[ 'Movie_Genre', 'Movie_Keywords', 'Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')


df_features.shape

df_features
x = df_features['Movie_Genre'] + '' + df_features['Movie_Keywords'] + '' + df_features['Movie_Tagline'] +''+ df_features['Movie_Cast']+ ''+ df_features['Movie_Director']


x

x.shape
#Get Feature Text Conversion to Tokens

from sklearn.feature_extraction.text import TfidfVectorizer



tfidf = TfidfVectorizer()



x = tfidf.fit_transform(x)



x.shape
print(x)
# Get Similarity Score using Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity



Similarity_Score = cosine_similarity(x)



Similarity_Score
Similarity_Score.shape
# Get Movie Name as Input from User and Validate for Closest Spelling

Favourite_Movie_Name = input(' Enter your favourite movie name :') # Remove accidental indentation here



All_Movies_Title_List = df['Movie_Title'].tolist()


import difflib


Movie_Recommendation = difflib.get_close_matches (Favourite_Movie_Name, All_Movies_Title_List)
print(Movie_Recommendation)



Close_Match = Movie_Recommendation[0]
print (Close_Match)


Index_of_Close_Match_Movie = df [df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)


# getting a list of similar movies

Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print (Recommendation_Score)

#Get All Movies Sorted Based on Recommendation Score for your Favourite Movie
#sorting the movies based on their similarity score

Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse=True)
print (Sorted_Similar_Movies)
print('Top 30 Movies Suggested for You :\ n ')

i=1

for movie in Sorted_Similar_Movies:
   index = movie[0]
   title_from_index = df [df.index==index]['Movie_Title'].values[0]
   if (i<31):
    print(i, '.',title_from_index)
    i+=1

    #Top 10 Movies Recommended Based on Your Favorite Movie
    import difflib

Movie_Name = input('Enter your favorite movie name: ')

list_of_all_titles = df['Movie_Title'].tolist()

# Find close matches to the input movie name
close_matches = difflib.get_close_matches(Movie_Name, list_of_all_titles)

if close_matches:
    closest_match = close_matches[0]  # Get the closest match
    Index_of_Movie = df[df.Movie_Title == closest_match]['Movie_ID'].values[0]

    Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))

    sorted_similar_movies = sorted(Recommendation_Score, key=lambda x: x[1], reverse=True)

    print('Top 10 Movies suggested for you: \n')

    i = 1

    for movie in sorted_similar_movies:
        index = movie[0]
        if index < len(df):
            title_from_index = df[df.Movie_ID == index]['Movie_Title'].values[0]
            print(i, '.', title_from_index)
            i += 1
        else:
            print("Invalid index:", index)

        if i > 10:
            break
else:
    print('No close matches found for the entered movie name.')