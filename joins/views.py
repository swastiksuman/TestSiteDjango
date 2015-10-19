from django.shortcuts import render

# Create your views here.
from .forms import EmailForm
from .models import Join


def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip



def home(request):

    print(request.META.get("REMOTE_ADDR"))
    form = EmailForm(request.POST)
    if form.is_valid():
        new_join = form.save(commit=False)
        #email = form.cleaned_data['email']
        #new_join, created = Join.objects.get_or_create(email=email)
        #print(new_join, created)
        new_join.ip_address = get_ip(request)
        new_join.save()


    context={"form": form}
    template = "home.html"
    return render(request, template, context)

def home2(request):

    context={}
    template = "home2.html"
    return render(request, template, context)

