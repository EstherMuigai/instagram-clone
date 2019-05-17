from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^profile$',views.profile,name = 'profile'),
    url(r'^timeline$', views.timeline, name='timeline'),
]

    