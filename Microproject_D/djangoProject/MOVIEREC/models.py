from django.db import models

class Genrecinema(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Crime', 'Crime'),
        ('Sports', 'Sports'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Biography', 'Biography'),
        ('Romance', 'Romance'),
        ('Sci-fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
        ('War', 'War'),
    ]

    Moviename = models.CharField(max_length=255)
    Genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    IMDB = models.DecimalField(max_digits=3, decimal_places=2)
    Rottentomatoes = models.DecimalField(max_digits=3, decimal_places=0)
    Universe = models.CharField(max_length=255, null=True)
    Director = models.CharField(max_length=255)
    Description = models.TextField()
    date = models.DateField()
    Movieimage = models.URLField(max_length=255)

# Create your models here.
