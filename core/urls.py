from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("admin/", admin.site.urls),
]
