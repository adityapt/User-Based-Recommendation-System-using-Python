# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:55:23 2015

"""

print ()

##################################
# data set for collaborative filtering 
##################################
     
songData = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

###################################
## User Based filtering 
###################################

# import UserBasedFiltering module
import UserBasedFiltering

# manhattan NN
# ANS: [('Broken Bells', 4.0), ('Deadmau5', 1.0), ('Vampire Weekend', 1.0)]
ubf = UserBasedFiltering.UserBasedFilteringRecommender(songData, metric='minkowski', r=1)
print ("UBF NN Manhattan Recommendation for Veronica:")
print(ubf.recommendKNN('Veronica'))

print ()

# euclidean NN
# ANS: [('Broken Bells', 4.0), ('Deadmau5', 1.0), ('Vampire Weekend', 1.0)]
ubf = UserBasedFiltering.UserBasedFilteringRecommender(songData, metric='minkowski', r=2)
print ("UBF NN Euclidean Recommendation for Veronica:")
print(ubf.recommendKNN('Veronica'))

print ()

# minkowski (r=3) NN 
# ANS: [('Broken Bells', 4.0), ('Deadmau5', 1.0), ('Vampire Weekend', 1.0)]
ubf = UserBasedFiltering.UserBasedFilteringRecommender(songData, metric='minkowski', r=3)
print ("UBF NN Minkowski (r=3) Recommendation for Veronica:")
print(ubf.recommendKNN('Veronica'))

print ()

# cosine NN
# ANS: [('Broken Bells', 4.5), ('Deadmau5', 4.0), ('Vampire Weekend', 4.0)]
ubf = UserBasedFiltering.UserBasedFilteringRecommender(songData, metric='cosine')
print ("UBF NN Cosine Recommendation for Veronica:")
print(ubf.recommendKNN('Veronica'))

print ()

# pearson NN
# ANS: [('Broken Bells', 2.0), ('Vampire Weekend', 2.0)]
ubf = UserBasedFiltering.UserBasedFilteringRecommender(songData, metric='pearson')
print ("UBF NN Pearson Recommendation for Veronica:")
print(ubf.recommendKNN('Veronica'))

print ()

# pearson KNN with k=3
# ANS: [('Broken Bells', 2.64), ('Vampire Weekend', 2.2), ('Deadmau5', 1.71)]
ubf = UserBasedFiltering.UserBasedFilteringRecommender(songData, metric='pearson', k=3)
print ("UBF KNN (k=3) Pearson Recommendation for Veronica:")
print(ubf.recommendKNN('Veronica'))

print()

