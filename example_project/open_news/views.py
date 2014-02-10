# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
#shortcut version
from django.shortcuts import render

from open_news.models import Article, Article2
from django.template import RequestContext
from django.shortcuts import render_to_response
import os
import shlex
import subprocess

def index(request):
	queryset = Article.objects.all()
	template = loader.get_template('open_news/index.html')
	context = RequestContext(request, {'queryset': queryset})
	return HttpResponse(template.render(context))

def index2(request):
	queryset2 = Article2.objects.all()
	template2 = loader.get_template('open_news/PSEiIndex.html')
	context2 = RequestContext(request, {'queryset2': queryset2})
	return HttpResponse(template2.render(context2))

def detail(request, myID):
	return HttpResponse("You're looking at link %s." % myID)

def run_script(request):
	if request.method == 'POST':
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")
		subprocess.call(["python", "run.py"])

	queryset = Article.objects.all()
	template = loader.get_template('open_news/index.html')
	context = RequestContext(request, {'queryset': queryset})
	return HttpResponse(template.render(context))

def amchart(request):
	template = loader.get_template('open_news/chart.html')
	return render_to_response(template)





