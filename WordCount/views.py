from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html',{'u_r_curious':'<3 u 3000!!!'})
def b2(request):
    #return HttpResponse("<h1>Ritesh's corner</h1> heck ya motherfuckers learning django!!!<br></br>")
    return render(request,'authorsprofile.html')
def count(request):
    ft=request.GET['fulltext']
    #print(ft)
    wordlist = ft.split(' ')
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add to the dictionary
            worddictionary[word]=1
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = False)
    return render(request,'count.html',{'fulltext':ft,'count':len(wordlist),'sortedwords':sortedwords})

def wordbox(request):
    return render(request,'wordbox.html',{'u_r_curious':'<3 u 3000!!!'})




