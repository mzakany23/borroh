from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from product.models import Product

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

def product_detail_non_json(request,id):
	try:
		product = Product.objects.get(id=id)
	except:
		product = None
	template = 'product/product-detail.html'
	context={'product' : product}
	return render(request,template,context)