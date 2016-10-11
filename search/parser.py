from search.reviewCollection import reviewCollection

def parseReviews():
	flag = True
	review_list = open("foods.txt")
	review_dict = {}
	if(flag):
		for line in review_list:
			if(line=="\n"):
				obj = reviewCollection()
				obj.add(review_dict)
				review_dict.clear()
			else:
				line = line.split(':')
				if "productId" in line[0]:
					review_dict.update({'productId':line[1].strip()})
				elif "userId" in line[0]:
					review_dict.update({'userId':line[1].strip()})
				elif "profileName" in line[0]:
					review_dict.update({'profileName':line[1].strip()})
				elif "helpfulness" in line[0]:
					review_dict.update({'helpfulness':line[1].strip()})
				elif "score" in line[0]:
					review_dict.update({'score':line[1].strip()})
				elif "time" in line[0]:
					review_dict.update({'time':line[1].strip()})
				elif "summary" in line[0]:
					review_dict.update({'summary':line[1].strip()})
				elif "text" in line[0]:
					review_dict.update({'text':line[1].strip()})
		flag = False