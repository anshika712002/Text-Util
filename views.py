# from django.http import HttpResponse
# INTRO
# def index(request):
#     return HttpResponse ("Hello Anshika")
# def about(request):
#     return HttpResponse ("Hello Anshika ji")
# EXERCISE 1
# def index(request):
#     s='''<h1>HOME<br><h1>
#     <a href="https://www.codewithharry.com/videos/"> Code With Harry </a> <br> 
#     <a href="https://www.w3schools.com/python/"> W3 School  </a> <br> 
#     <a href="https://openai.com/chatgpt/">Chat GPT </a>   <br>
#     <a href="https://github.com/"> Git Hub  </a> <br>
#     <a href="https://www.tutorialspoint.com/python/index.htm"> Tutorials Point</a>'''
#     return HttpResponse (s)


# #PIPELINE & templates
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request,'index.html')
# def about(request):
#     return HttpResponse ("About <a href='/'> BACK</a>")
# def removepunc(request):
#     #get the text
#     djtext=request.GET.get('TEXT','default')
#     #analyze text
#     print(djtext)
#     return HttpResponse ("Remove puncutation <a href='/'> BACK</a>")
# def capfirst(request):
#     return HttpResponse ("Captialize First <a href='/'> BACK</a>")
# def newlineremove(request):
#     return HttpResponse ("New line remove <a href='/'> BACK</a>")
# def spaceremover(request):
#     return HttpResponse ("Space remover <a href='/'> BACK</a>")
# def charcounter(request):
#     return HttpResponse ("Char counter <a href='/'> BACK</a>")

# templates
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    #check checkbox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcounter=request.GET.get('charcounter','off')
    #check if checkbox on
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analayzed=""
        for char in djtext:
            if char not in punctuations:
                analayzed=analayzed+char
        params={'purpose':'remove punctuation','analyzed_text':analayzed}
        djtext=analayzed
    if(fullcaps=="on"):
        analayzed=""
        for char in djtext:
            analayzed=analayzed+char.upper()
            params={'purpose':'change to upper case','analyzed_text':analayzed}
            djtext=analayzed
    if(extraspaceremover=="on"):
        analayzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analayzed=analayzed+char
        params={'purpose':'remove the space','analyzed_text':analayzed}
        djtext=analayzed
    if(newlineremover=="on"):
        analayzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analayzed=analayzed+char
            params={'purpose':'new line remove','analyzed_text':analayzed}
            djtext=analayzed
    if(charcounter=="on"):
        count=0
        for char in djtext:
            if char.isalpha():
                count=count+1
                params={'purpose':'count the character','analyzed_text':count}
    if(removepunc!="on" and fullcaps!="on" and extraspaceremover!="on" and charcounter!="on" and newlineremover!="on"):
        return HttpResponse("ERROR!!! \n please select any operation to analyze.")      
    return render(request,'analyze.html',params)


    
    
