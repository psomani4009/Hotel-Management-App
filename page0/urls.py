from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('generate', views.gen, name='Generate Report'),
    path('dormitory', views.dorm, name='Dormitory'),
    path('c/<str:roomno>', views.checkout_room, name='Form Page'),
    path('<str:roomno>', views.assign_room, name='Form Page'),
]
