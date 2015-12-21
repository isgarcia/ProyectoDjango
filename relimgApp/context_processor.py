# coding: utf-8
from django.conf import settings
from relimgApp.models import *

#Se le pasa como unico argumento el request, a los procesadores de contexto
def SiteInfo(request):
	return {
		'site_title': settings.SITE_TITLE,
		'site_subtitle': settings.SITE_SUBTITLE,
		'site_credits': settings.SITE_CREDITS,
		'index_anime_description': settings.INDEX_ANIME_DESCRIPTION,
		'detail_title': settings.DETAIL_TITLE,
		'detail_type': settings.DETAIL_TYPE,
		'detail_state': settings.DETAIL_STATE,
		'detail_description': settings.DETAIL_DESCRIPTION,
		'detail_categories': settings.DETAIL_CATEGORIES,
	}