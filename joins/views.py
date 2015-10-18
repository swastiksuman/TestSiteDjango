from django.shortcuts import render

# Create your views here.
from .forms import EmailForm
from .models import Join
def home(request):

    print("ABC")
    form = EmailForm(request.POST)
    print(form.is_valid())
    #if form.is_valid():
    email = form.cleaned_data['email']
    new_join, created = Join.objects.get_or_create(email=email)
    print(new_join, created)

    print(new_join.timestamp)
    context={"form": form}
    template = "home.html"
    return render(request, template, context)

def home2(request):

    context={}
    template = "home2.html"
    return render(request, template, context)

