from django.shortcuts import render,redirect
from .models import movie
from .models import series
from .models import upcoming
from .models import chromovies
from .models import newlatest
from.models import newupcoming
from.models import newseries
# Create your views here.

def home(request):
    if request.user.is_authenticated:
       latests = newlatest.objects.all()
       return render(request,'index.html',{'data':latests})
    else:
        return redirect('login')
    
def movies(request):
    movies = movie.objects.all()
    return render(request,'movies.html',{'data':movies})

def chromoviess(request):
    movieschrono = chromovies.objects.all()
    return render(request,'chromovies.html',{'data':movieschrono})


def ser(request):
    webseries = newseries.objects.all()
    return render(request,'series.html',{'data':webseries})

def up(request):
    upcomings = newupcoming.objects.all()
    return render(request,'upcoming.html',{'data':upcomings})

def details(request,id):
    done = newlatest.objects.get(id = id)
    return render(request,'product-details.html',{'data':done})

def detailsmovies(request,id):
    mov = movie.objects.get(id = id)
    return render(request,'product-details.html',{'data':mov})

def detailschromovies(request,id):
    chro = chromovies.objects.get(id = id)
    return render(request,'product-details.html',{'data':chro})


def detailseries(request,id):
    siri = newseries.objects.get(id = id)
    return render(request,'product-details.html',{'data':siri})

def detailupc(request,id):
    upc = newupcoming.objects.get(id = id)
    return render(request,'product-details.html',{'data':upc})

def feedback(request):
     
    return render(request,'feedback.html')

def login(request):
     
    return render(request,'login.html')

def register(request):
     
    return render(request,'register.html')
