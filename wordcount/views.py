from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	dict = {
			"title":"First Django Page",
			"header":"My First Django site - Word Counter"
	}
	return render(request, 'home.html', dict)

def hostpage(request):
	return HttpResponse("<h1>Welcome to Sky Net!!!</h1>")

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddict = {}

	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1

	sorted_dict = sorted(worddict.items(), key=operator.itemgetter(1),reverse=True)

	dict ={
		"title"   			: "Count Page",
		"header"  			: "Welcome to Count page!!",
		"fulltext"			: fulltext,
		"count"   			: len(wordlist),
		"worddictcounter"   : sorted_dict
	}
	return render(request, 'count.html', dict)

def aboutUs(request):
	dict ={
		"title"   			: "About Us Page",
		"header"  			: "Welcome to About us!!",
	}
	return render(request, 'aboutus.html', dict)