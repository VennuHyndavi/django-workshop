from django.shortcuts import render
from django.http import HttpResponse
import operator 
# Create your views here.
def homepage(request):
    return render(request,"hello/home.html")
def about(request):
    return render(request,"hello/about.html")
def count(request):
    return render(request,"hello/count.html")
def count(request):
    fulltext=request.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    
    listof = list(word_dict.items())

    return render(request,'hello/count.html',{'fulltext':fulltext,'word_count':word_count,'listof':listof})   
