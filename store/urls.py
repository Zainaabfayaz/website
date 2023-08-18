from django.contrib import admin
from django.urls import path
from .views import Index , store
from .views import signup
from .views import login
from .views import Cart



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('cart' , Cart.as_view , name='cart'),

]