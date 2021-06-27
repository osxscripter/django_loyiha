from django.urls import path
from .views import StrimerReyting, BlogPost, AddPost

urlpatterns = [
    path('', StrimerReyting.as_view(), name='home'),
    path('blogs/', BlogPost.as_view(), name='blogs'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]