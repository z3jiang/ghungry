

from django.db import models

class Cafe(models.Model):
  id = models.CharField(max_length=32, primary_key=True, db_index=True)
  name = models.CharField(max_length=64, unique=True)
  last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

class MenuItem(models.Model):
  name = models.CharField(max_length=128)
  cafe = models.ForeignKey(Cafe, related_name='menuitems')

class Ingredient(models.Model):
  name = models.CharField(max_length=32)
  menu_item = models.ForeignKey(MenuItem, related_name='ingredients')
