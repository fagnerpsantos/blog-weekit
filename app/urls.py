from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('post/<int:id>', show_post, name='post')
]
