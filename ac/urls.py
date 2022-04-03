from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('Userlogin',views.ulogin,name="ulogin"),
    path('Userlogout',views.ulogout,name="ulogout"),

]