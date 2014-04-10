
from json_response import JSONResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse

import fetcher
from cafes import CAFES

def get_cafes(request):
  response = []
  for key, url in CAFES.items():
    response.append(fetcher.get(key, url))

  return JSONResponse(response, recursive=False)

def get_cafe(request, cafe_id):
  return JSONResponse(fetcher.get(cafe_id, CAFES[cafe_id]), recursive=True)
