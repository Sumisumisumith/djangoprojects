from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

#URLパターンを登録するためのリスト
urlpatterns = [
    #https://ホスト名/以下のパスが無の場合
    #viewsモジュールのindexviewを実効
    #URLパターン名は'index'
    path('', views.index_view, name='index'),
    path('blog-detail/<int:pk>/', views.blog_detail, name='blog_detail'),

    path('fashion-list/', views.fashion_view, name='fashion_list'),
    path('dailylife-list/', views.dailylife_view, name='dailylife_list'),
    path('sports-list/', views.sports_view, name='sports_list'),

    path('contact/', views.contact_view, name='contact')
]

