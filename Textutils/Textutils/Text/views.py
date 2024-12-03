from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    user_text=request.GET.get('text','default')
    result=request.GET.get('action','off')
    if result=="removepunc":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*'''
        analyzed=""
        for char in user_text:
            if char not in punctuations:
                analyzed+=char
        obj={'Analyzetext':analyzed}
        return render(request,'analyze.html',obj)
    elif result=='uppercase':
        cap=user_text.upper()
        obj={'capital':cap} 
        return render(request,'analyze.html',obj)
    elif result=='lowercase':
        low=user_text.lower()
        obj={'name':"Hari",'lower':low}
        return render(request,'analyze.html',obj)
    elif result=='count':
        cnt=len(user_text)
        obj={'name':"Hari",'charcount':cnt}
        return render(request,'analyze.html',obj)
    else:
        return HttpResponse("Error")

    
    