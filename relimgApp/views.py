from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from relimgApp.models import *

# Create your views here.
def index(request):
	anime_list = Anime.objects.order_by('title')
	context = {'anime_list' : anime_list}
	return render (request, 'index.html', context)

def details(request, anime_id):
	anime = get_object_or_404(Anime, pk=anime_id)
	context = {'anime' : anime, 'STATIC_URL' : settings.STATIC_URL}
	return render (request, 'details.html', context)
	#return HttpResponse('Ahora estas mirando el anime con ID: ' + anime_id)