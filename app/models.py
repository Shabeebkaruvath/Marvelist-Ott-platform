 
from unicodedata import name
from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.TextField
    url= models.URLField
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class series(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class upcoming(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class chromovies(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)


class newlatest(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=5000)
    url= models.CharField(max_length=5000)
    svedio =  models.CharField(max_length=5000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newmovie(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=5000)
    url= models.CharField(max_length=5000)
    svedio =  models.CharField(max_length=5000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newseries(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=5000)
    url= models.CharField(max_length=5000)
    svedio =  models.CharField(max_length=5000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newupcoming(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=5000)
    url= models.CharField(max_length=5000)
    svedio =  models.CharField(max_length=5000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newchromovies(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=5000)
    url= models.CharField(max_length=5000)
    svedio =  models.CharField(max_length=5000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)