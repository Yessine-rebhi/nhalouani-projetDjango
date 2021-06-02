from django.urls import path,include
from django.conf.urls import url
from . import views
from register import views as v
urlpatterns = [ 
    path('vitrine',views.vitrine,name="vitrine"),  
    path('forni',views.forni,name="forni"),
    path('forniprod/<id>',views.forniprod,name="forniprod"),
    path('', views.index),
    path("register/", v.register, name="register"),
#url(r'^$', views.mesProduits, name='mesProduits'),
]
