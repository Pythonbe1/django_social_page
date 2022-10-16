from django.urls import path
from . import views

urlpatterns = [
    path('beka/', views.index)

]

