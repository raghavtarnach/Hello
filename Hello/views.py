from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1
    
    return render(request,'count.html',{'fulltext':text, 'count':len(wordlist),'mostocc':worddic})

def about(request):
    return render(request,'about.html')