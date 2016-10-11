from search.reviews import Reviews

class reviewCollection:
	reviewCollectionList = []
	flag = True
	def add(self,review_dict):
		if(reviewCollection.flag):
			review = Reviews(review_dict["productId"],review_dict["userId"],review_dict["profileName"],review_dict["helpfulness"],review_dict["score"],review_dict["time"],review_dict["summary"],review_dict["text"])
			reviewCollection.reviewCollectionList.append(review)
		