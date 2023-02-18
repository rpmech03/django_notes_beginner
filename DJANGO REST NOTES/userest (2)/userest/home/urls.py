from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('delete', views.delete,name="delete"),
    path('update', views.update,name="update"),
    path('search', views.search,name="search"),
    path('sendmail', views.sendmail,name="sendmail"),
    path('verify', views.verify,name="verify"),
]