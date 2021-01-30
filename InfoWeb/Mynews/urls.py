from django.urls import path
from Mynews.views import *

app_name = 'Mynews'

urlpatterns = [
    # /blog/
    path('', PostLV.as_view(), name='index'),

    # /blog/post
    path('post/', PostLV.as_view(), name='post_list'),

    # /blog/post/{slug}
    path('post/<str:pk>/', PostDV.as_view(), name='post_detail'),

    # Search: /search/ -> http://127.0.0.1:8000/blog/search/
    path('search/', SearchFormView.as_view(), name='search'),
    path('refresh', RefreshFormView.as_view(), name='refresh'),
]
