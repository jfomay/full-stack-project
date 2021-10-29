from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.date_released}'


class Character(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.movie.title}: {self.first_name} {self.last_name}'

