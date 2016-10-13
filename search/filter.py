# This module filters the top 20 reviews in the result set and 
# send dictionary data to the request in the views.py, that is then rendered in out template

from __future__ import division
from search.reviews import Reviews
from search.index import Index
from search.reviewCollection import reviewCollection

def fetchReviewData(query):
	review_data = []
	keywordHash = Index.hashMap
	reviewList = reviewCollection.reviewCollectionList
	review_index = 0
	n = len(query)
	result = {}
	scoreList = []
	filteredReviewIndexList = []
	for term in query:
		if term in keywordHash:
			temp = keywordHash[term]
			filteredReviewIndexList.extend(temp)

	filteredReviewIndexList = list(set(filteredReviewIndexList))

	for index in filteredReviewIndexList:
		review = reviewList[index]
		count = 0
		for term in query:
			if term in keywordHash:
				temp = keywordHash[term]
				if index in temp:
					count = count + 1
		score = count/n
		if score not in scoreList and count>0:
			scoreList.append(score)
			l = []
			l.append(index)
			result.update({score:l})
		elif score in scoreList and count>0:
			l = result[score]
			l.append(index)
			result.update({score:l})

	review_data = getReviewData(scoreList,result)	
	return review_data


def getReviewData(scoreList,result):
	reviewList = reviewCollection.reviewCollectionList
	scoreList.sort(reverse = True)
	reviews = []
	for score in scoreList:
		if len(reviews)>20:
			break
		else:
			reviews.append(result[score])
	review_data = []
	score_index = 0
	count = 0
	for item in reviews:
		if(count>20):
			break
		count = count + len(item)
		if(count>20):
			t = count - len(item)
			t = 20 - t
			item = item[0:t]
		for i in item:
			review = reviewList[i]
			review_info = {}
			review_info.update({"productId":review.productId})
			review_info.update({"userId":review.userId})
			review_info.update({"profileName":review.profileName})
			review_info.update({"helpfulness":review.helpfulness})
			review_info.update({"score":review.score})
			review_info.update({"time":review.time})
			review_info.update({"summary":review.summary})
			review_info.update({"text":review.text})
			review_info.update({"searchScore":scoreList[score_index]})
			review_data.append(review_info)
		score_index = score_index + 1
	return review_data