from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('url/', views.rss_list, name='url_list'),   # 一覧
    path('url/add/', views.rss_edit, name='url_add'),  # 登録
    path('url/mod/<int:url_id>/', views.rss_edit, name='url_mod'),  # 修正
    path('url/del/<int:url_id>/', views.rss_del, name='url_del'),   # 削除
]
