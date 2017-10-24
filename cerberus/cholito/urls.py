from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^denunciar/$', views.denunciar, name='denunciar'),
    url(r'^registrarse/$', views.crear_usuario, name='signUp'),
    url(r'^denuncia/(?P<id>[0-9]+)/$', views.ficha_denuncia, name='ficha_denuncia'),
    url(r'^animal/(?P<id>[0-9]+)/$', views.ficha_animal, name='ficha_animal'),
]
