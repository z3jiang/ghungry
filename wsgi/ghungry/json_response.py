
import json
from django.http import HttpResponse
from cafe import *

class CafeEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Cafe):
      return {'items': obj.items}
    elif isinstance(obj, MenuItem):
      return {'name': obj.name, 'ingredients': obj.ingredients}
    elif isinstance(obj, Ingredient):
      return {'name': obj.name}
    else:
      # Let the base class default method raise the TypeError
      return json.JSONEncoder.default(self, obj)

def JSONResponse(obj):
  return HttpResponse(json.dumps(obj, cls=CafeEncoder, indent=2),
                      content_type="application/json")

