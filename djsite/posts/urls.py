import profile

from django.contrib.messages import add_message
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('day/<int:day_id>/', show_day, name='day'),
    path('add_post/', add_post, name='add_post'),
    path('profile', profile, name='profile'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('obj/<int:obj_id>/', show_obj, name='obj'),
    path('review/<int:pk>/', AddMessage.as_view(), name='add_mes'),
    path('chats', chats, name='chats'),
    path('chat/<int:object_id>', show_chat, name='show_chat')

]