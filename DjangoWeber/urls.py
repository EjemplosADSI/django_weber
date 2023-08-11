from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("user_profile.urls")),
    path("busine/", include("business.urls")),
]
