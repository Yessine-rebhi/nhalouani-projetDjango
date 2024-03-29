from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from register import views as v

urlpatterns = [
    url(r'^$',views.index),
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('magasin/', include('magasin.urls')),
    path('', include("django.contrib.auth.urls")),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
