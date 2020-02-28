from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='main'),
    url(r'^sith$', views.sith_form, name='sith_form'),
    url(r'^recurt/$', views.recurt, name='recurt_info'),
    url(r'^task$', views.task, name='task'),
    url(r'^recurt_form$', views.recurt_form, name='recurt_form'),
    url(r'^shadowhand_form$', views.shadowhand_form, name='shadowhand_form'),
    url(r'^shadowhand/$', views.shadow_hand, name='shadowhand_info'),
]