from django.shortcuts import render

def home(request):


    context={"form":form}
    template = "home.html"
    return render(request, template, context)

def home2(request):

    context={}
    template = "home2.html"
    return render(request, template, context)
