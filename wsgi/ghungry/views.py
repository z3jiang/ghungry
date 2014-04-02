import os
from cafe import *
from json_response import JSONResponse
from bs4 import BeautifulSoup
from django.shortcuts import render_to_response
from django.http import HttpResponse
import urllib2

CAFES = {
  'beta': 'http://menu-mtv-beta.blogspot.com',
  'charlies': 'http://menu-mtv-charlies.blogspot.com',
}

def _soupfy(url):
  response = urllib2.urlopen(url)
  return BeautifulSoup(response)

def list_cafes(request):
  response = []
  for key, url in CAFES.items():
    response.append({key: Cafe(_soupfy(url))})

  return JSONResponse(response)

def get_menu_by_cafe(request, cafe_id):
  return HttpResponse()
