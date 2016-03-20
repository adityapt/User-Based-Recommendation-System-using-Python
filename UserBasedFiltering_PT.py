# -*- coding: utf-8 -*-
"""
Mining Assignment 1
"""

import math

#################################################
# recommender class does user-based filtering and recommends items 
class UserBasedFilteringRecommender:
    
    # class variables:    
    # none
    
    ##################################
    # class instantiation method - initializes instance variables
    #
    # usersItemRatings:
    # users item ratings data is in the form of a nested dictionary:
    # at the top level, we have User Names as keys, and their Item Ratings as values;
    # and Item Ratings are themselves dictionaries with Item Names as keys, and Ratings as values
    # Example: 
    #     {"Angelica":{"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
    #      "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}}
    #
    # metric:
    # metric is in the form of a string. it can be any of the following:
    # "minkowski", "cosine", "pearson"
    #     recall that manhattan = minkowski with r=1, and euclidean = minkowski with r=2
    # defaults to "pearson"
    #
    # r:
    # minkowski parameter
    # set to r for minkowski, and ignored for cosine and pearson
    #
    # k:
    # the number of nearest neighbors
    # defaults to 1
    #
    def __init__(self, usersItemRatings, metric='pearson', r=1, k=1):
        
        # set self.usersItemRatings
        self.usersItemRatings = usersItemRatings

        # set self.metric and self.similarityFn
        if metric.lower() == 'minkowski':
            self.metric = metric
            self.similarityFn = self.minkowskiFn
        elif metric.lower() == 'cosine':
            self.metric = metric
            self.similarityFn = self.cosineFn
        elif metric.lower() == 'pearson':
            self.metric = metric
            self.similarityFn = self.pearsonFn
        else:
            print ("    (DEBUG - metric not in (minkowski, cosine, pearson) - defaulting to pearson)")
            self.metric = 'pearson'
            self.similarityFn = self.pearsonFn
        
        # set self.r
        if (self.metric == 'minkowski'and r > 0):
            self.r = r
        elif (self.metric == 'minkowski'and r <= 0):
            print ("    (DEBUG - invalid value of r for minkowski (must be > 0) - defaulting to 1)")
            self.r = 1
            
        # set self.k
        if k > 0:   
            self.k = k
        else:
            print ("    (DEBUG - invalid value of k (must be > 0) - defaulting to 1)")
            self.k = 1
            
    
    #################################################
    # minkowski distance (dis)similarity - most general distance-based (dis)simialrity measure
    # notation: if UserX is Angelica and UserY is Bill, then:
    # userXItemRatings = {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    # userYItemRatings = {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    def minkowskiFn(self, userXItemRatings, userYItemRatings):
        
        distance = 0
        commonRatings = False 
        
        for item in userXItemRatings:
            # inlcude item rating in distance only if it exists for both users
            if item in userYItemRatings:
                distance += pow(abs(userXItemRatings[item] - userYItemRatings[item]), self.r)
                commonRatings = True
                
        if commonRatings:
            return round(pow(distance,1/self.r), 2)
        else:
            # no ratings in common
            return -2

    #################################################
    # cosince similarity
    # notation: if UserX is Angelica and UserY is Bill, then:
    # userXItemRatings = {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    # userYItemRatings = {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    def cosineFn(self, userXItemRatings, userYItemRatings):
        
        sum_xy = 0
        sum_x2 = 0
        sum_y2 = 0
        
        for item in userXItemRatings:
            if item in userYItemRatings:
                x = userXItemRatings[item]
                y = userYItemRatings[item]
                sum_xy += x * y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        
        denominator = math.sqrt(sum_x2) * math.sqrt(sum_y2)
        if denominator == 0:
            return -2
        else:
            return round(sum_xy / denominator, 3)

    #################################################
    # pearson correlation similarity
    # notation: if UserX is Angelica and UserY is Bill, then:
    # userXItemRatings = {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    # userYItemRatings = {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    def pearsonFn(self, userXItemRatings, userYItemRatings):
        
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        
        for item in userXItemRatings:
            if item in userYItemRatings:
                n += 1
                x = userXItemRatings[item]
                y = userYItemRatings[item]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
       
        if n == 0:
            return -2
        
        denominator = math.sqrt(sum_x2 - pow(sum_x, 2) / n) * math.sqrt(sum_y2 - pow(sum_y, 2) / n)
        if denominator == 0:
            return -2
        else:
            return round((sum_xy - (sum_x * sum_y) / n) / denominator, 2)
            

    #################################################
    # make recommendations for userX from the most similar k nearest neigibors (NNs)
    def recommendKNN(self, userX):
        
        # YOUR CODE HERE
        
        # for given userX, get the sorted list of users - by most similar to least similar        
        
        # calcualte the weighted average item recommendations for userX from userX's k NNs
        
        # return sorted list of recommendations (sorted highest to lowest ratings)
        
        ratings = self.usersItemRatings # space reduction to write the code easily 
        datakeys = list(ratings)
        
        # creating a list that contains all the songs
        songslist = []        
        for i in ratings:
            for j in list(ratings[i]):
                songslist.append(j)
        songslist = list(set(songslist))
            
        # creating the list of songs that are not rated by userX        
        userxnotrated = []   
        
        if userX in ratings:
            for i in songslist:
                if i not in list(ratings[userX]):
                    userxnotrated.append(i)
        # If the user is not present in the list, then it will print the following statements and 
        # return an empty list at the end
        else:
            print()
            print('The User is not in the list')
            print()
            print('please make sure you are considering the case sensitivity of the user names')
        
        # getting the output of the correlation parameters in a similarity dictionary        
        similarity = {} 
        
        for i in range(len(list(ratings))):
            if userX in ratings and userX != datakeys[i]:
                if self.metric.lower() == 'pearson':
                    similarity[datakeys[i]] = self.pearsonFn(ratings[userX],ratings[datakeys[i]])
                elif self.metric.lower() == 'cosine':
                    similarity[datakeys[i]] = self.cosineFn(ratings[userX],ratings[datakeys[i]])
                else:
                    similarity[datakeys[i]] = self.minkowskiFn(ratings[userX],ratings[datakeys[i]])
           
#        return similarity
        
        # taking only the k sorted values from the similarity dictionary
        sortedtillk = {}
        
        if self.metric == 'pearson' or self.metric == 'cosine':
            values = list(sorted(similarity.values()))
            values.reverse()            
            similaritysorted = values[:self.k]
        else:
            similaritysorted = sorted(similarity.values())[:self.k]
        
        # making sure that i am mapping back 
        for i,j in similarity.items():
            if j in similaritysorted:
                sortedtillk[i] = j
        
        # in case the number selected is more than k due to same lengths, then
        # taking the user who has rated more songs and breaking the tie
        length = {}
        if len(sortedtillk.keys()) > self.k:
            for i,j in sortedtillk.items():
                if list(sortedtillk.values()).count(j) >1:
                    length[i] = len(ratings[i].keys())
                    
#        return length
        l = list(sortedtillk.keys())
        
        for i in l:
            if list(sortedtillk.values()).count(j) >1:         
                if len(ratings[i].keys()) < max(length.values()):
                    del sortedtillk[i]
                     
#        return sortedtillk, length
        # transforming pearson and cosine
        pearsortedtillk = {}
        if self.metric == 'pearson' or self.metric == 'cosine':
            for i in sortedtillk.keys():
                pearsortedtillk[i] = (sortedtillk[i]+1)*0.5
        
        else:
            pearsortedtillk = sortedtillk
            
                             
        # calculating the weights
        sumk = 0
        weights = {}                        
        for i in pearsortedtillk:
            sumk = sumk + pearsortedtillk[i]
            
        for i in pearsortedtillk:
            weights[i] = pearsortedtillk[i]/sumk 
        
        # calculating the average recommended ratings of the songs
        
        weight = {}
        
      
        for i in userxnotrated:
            rating = 0            
            for j in sorted(weights.keys()):               
                if i in self.usersItemRatings[j]:
                    rating  = rating+ self.usersItemRatings[j][i]*weights[j]
                    weight[i] = round(rating,2)
        
        
        # returning the list of recommended songs in the sorted order
        recommend = []
        ls = sorted(list(weight.values()))
        ls.reverse()
        for i in ls:
            for j in weight.keys():
                if weight[j] == i:
                    if (j,i) not in recommend:
                        recommend.append((j,i))
                              
                       
        return recommend
        
        
                    
                    
            
                
                
        
            
        
        
        
        
        
                
            
        
        
                    
                    
                    
                    
                
            
        


        
