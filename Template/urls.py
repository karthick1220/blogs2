# from django.urls import path  
# from Template import views  
# urlpatterns = [  
#     path('', views.index,name='home'),  
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^more/$', views.MorePageView.as_view(), name='more'),
]