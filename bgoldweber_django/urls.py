from django.urls import path, include, re_path
from django.contrib import admin
from django.views.static import serve

from bgoldweber_django import settings

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('playground/', include('playground.urls')),
    # path('playground/', include('playground.urls')),
    path('admin/', admin.site.urls),
    path('', include('cv.urls')),
    path('blog/', include('blog.urls'))
]
