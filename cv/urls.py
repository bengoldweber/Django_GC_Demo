from django.template.defaulttags import url
from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='cv/resume'),
]