from django.db import models

class User(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  top_list = models.ForeignKey('Toplist', blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.id}, {self.name}'
  


class Toplist(models.Model):
  author = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
  burger_places = models.ManyToManyField('BurgerPlace')

  def __str__(self):
    return f'{self.author}s list'

class BurgerPlace(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  
  def __str__(self):
    return f'{self.name}'

  