
_STRIP = u'\n\t \u200b\u2009*'

class Ingredient(object):
  def __init__(self, name):
    self.name = name

class MenuItem(object):
  def __init__(self, name, ingredients):
    self.name = name
    self.ingredients = ingredients

class Cafe(object):
  def __init__(self, soup):
    self.items = []
    for item in soup.find_all(attrs={'class': 'menu-item'}):
      name = item.find(attrs={'class': 'menu-item-name'}).text
      name = name.strip(_STRIP)
      if name.startswith('R*'):
        name = name[2:].strip(_STRIP)

      ingredients = item.find(attrs={'class': 'menu-item-ingredients'}).text
      ingredients = ingredients.split(',')
      ingredient_objs = [Ingredient(ingredient_name.strip(_STRIP)) 
        for ingredient_name in ingredients]
      self.items.append(MenuItem(name, ingredient_objs))

