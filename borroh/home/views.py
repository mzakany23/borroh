from django.shortcuts import render

def home(request):
	context = {}
	template = 'layouts/base.html'
	return render(request,template,context)
