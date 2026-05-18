from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]