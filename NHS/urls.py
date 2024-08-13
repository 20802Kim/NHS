# 프로젝트 폴더의 urls.py

from django.contrib import admin
# from .admin import admin
from django.urls import include, path
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('NHSApp/', include('NHSApp.urls')),
]
