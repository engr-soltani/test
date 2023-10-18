from django.urls import path

from .views.post_view import PostView
from .views.post_rate_view import PostRateView

urlpatterns =[
     path('post/',PostView.as_view(),name='post'),
     path('getPosts/',PostView.as_view(),name='getPosts'),
     path('postRate/',PostRateView.as_view(),name='postRate')
]