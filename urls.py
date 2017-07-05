from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.company_new, name='company_new'),

]