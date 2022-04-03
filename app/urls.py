from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('movies',views.movies,name="movies"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('chromovies',views.chromoviess,name="chromovies"),
    path('series',views.ser,name="series"),
    path('details/<int:id>',views.details,name="details"),
    path('detailsmovies/<int:id>',views.detailsmovies,name="detailsmovies"),
    path('detailschromovies/<int:id>',views.detailschromovies,name="detailschromovies"),
    path('detailseries/<int:id>',views.detailseries,name="detailseries"),
    path('detailupc/<int:id>',views.detailupc,name="detailupc"),
    path('upcoming',views.up,name="upcoming")
     
]
