from django.urls import path, include, re_path
from django.contrib import admin
from django.views.static import serve

from bgoldweber_django import settings

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    # path('playground/', include('playground.urls')),
    # path('playground/', include('playground.urls')),
    path('admin/', admin.site.urls),
    path('', include('cv.urls'))
]
