from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.LogIn,name='login'),
    path('logout/',views.LogOut,name='logout')
]
