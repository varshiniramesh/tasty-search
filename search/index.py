import re
from search.reviewCollection import reviewCollection

# Index is built for the dataset, suitable for implementing search
# a hashMap that maps any given keyword with the list of review objects in the ReviewCollection 
# Container that contains the keyword
class Index():
	hashMap = {}
	flag = True
	def buildIndexes(self):
		if(Index.flag):
			reviewList = reviewCollection.reviewCollectionList
			review_index = 0
			r = re.compile(r'[^a-z]+')
			for review in reviewList:
				review_text = review.text.split(" ")
				for word in review_text:
					word = r.sub('',word)
					if word in Index.hashMap:
						if review_index not in Index.hashMap[word]:
							Index.hashMap[word].append(review_index)
					else:
						Index.hashMap[word] = [review_index]
				review_index = review_index+1
		Index.flag = False

