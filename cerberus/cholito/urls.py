from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^denunciar/$', views.denunciar, name='denunciar'),
    url(r'^registrarse/$', views.crear_usuario, name='signUp'),
]
