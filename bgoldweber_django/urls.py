from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # path('playground/', include('playground.urls')),
    # path('playground/', include('playground.urls')),
    path('admin/', admin.site.urls),
    path('', include('cv.urls'))
]
