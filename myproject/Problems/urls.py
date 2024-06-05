from django.urls import path
from .import views


urlpatterns = [

    path('',views.problemSet,name='problem'),
    path('show/',views.show_table,name='show_database')
    
]
