from django.shortcuts import render
from django.shortcuts import redirect
from search.parser import parseReviews
from search.index import Index
from search.filter import fetchReviewData
from search.reviewCollection import reviewCollection

# Create your views here.
def index(request):
	parseReviews()
	index = Index()
	index.buildIndexes()
	content = {}
	if request.method=='GET' and 'query' in request.GET:
		query = request.GET.get('query')
		print query,"QUERY"
		if(query!=""):
			query = query.replace(","," ")
			query_set = query.split(" ")
			query = query.replace(" ",",")
			data = fetchReviewData(query_set)
			content={'data':data,'query':query}
	return render(request,'search/index.html',content)


