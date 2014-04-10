
import logging
_logger = logging.getLogger(__name__)

from datetime import datetime, timedelta

from bs4 import BeautifulSoup
import urllib2
from cafes import CAFES
from models import *
import cafe_parser

_STRIP = u'\n\t \u200b\u2009*'

def parse_and_persist(soup, cafe):
  for item in soup.find_all(attrs={'class': 'menu-item'}):
    name = item.find(attrs={'class': 'menu-item-name'}).text
    name = name.strip(_STRIP)
    if name.startswith('R*'):
      name = name[2:].strip(_STRIP)

    _logger.debug('found item %s' % name)
    menuitem = MenuItem(cafe=cafe, name=name)
    menuitem.save()

    ingredients = item.find(attrs={'class': 'menu-item-ingredients'}).text
    ingredients = ingredients.split(',')
    for ingredient in ingredients:
      _logger.debug('  found ingredient %s' % ingredient)
      ingredient = ingredient.strip(_STRIP)
      ingredient = Ingredient(menu_item=menuitem, name=ingredient)
      ingredient.save()


def _soupfy(url):
  _logger.info('reading url %s' % url)
  response = urllib2.urlopen(url)
  return BeautifulSoup(response)

def get(cafe_id, url, fetch=True):
  date_filter = datetime.now() - timedelta(minutes=15)
  found = Cafe.objects.filter(pk=cafe_id, last_modified__gt=date_filter) \
                      .select_related('menuitems') \
                      .select_related('menuitems__ingredients') \

  if found:
    _logger.info('%s is cached' % cafe_id)
    # There should only be one match.
    return found

  if fetch:
    _logger.info('fetching %s' % cafe_id)
    soup = _soupfy(url)
    cafe = Cafe(id=cafe_id, name=cafe_id)
    cafe.save()
    parse_and_persist(soup, cafe)
    return get(cafe_id, url, fetch=False)

  return None

