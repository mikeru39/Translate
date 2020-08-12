from django.urls import path
from example import views

app_name = 'example'

urlpatterns = [
    path('',
         views.index,
         name='home')
]
