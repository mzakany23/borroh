from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

from models import Product

def product_detail(request,id):	
	try:
		product = Product.objects.get(id=id)
		images = product.image_set.all()[0]
	except:
		product = None
	
	product_serialized = serializers.serialize("json",[product,images])


	return HttpResponse(
            json.dumps(product_serialized),
            content_type="application/json")

