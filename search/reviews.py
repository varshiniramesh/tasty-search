# Reviews class defines the structure of each review
#getSCore , assigns a score the review object based on the query set
class Reviews:
	def __init__(self,productId,userId,profileName,helpfulness,score,time,summary,text):
		self.productId = productId
		self.userId = userId
		self.profileName = profileName
		self.helpfulness = helpfulness
		self.score = score
		self.time = time
		self.summary = summary
		self.text = text

	def getScore(self,query_set):
		text = self.text
		total_count = len(query_set)
		count = 0
		for word in query_set:
			if word in text:
				count = count + 1
		score = count/total_count
		return score


