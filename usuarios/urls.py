from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^perfil/(?P<pk>[0-9]+)/$', views.perfil_detail)
]
