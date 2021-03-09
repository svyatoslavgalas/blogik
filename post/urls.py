from django.urls.conf import path

from . import views

app_name = 'post'


urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>/delete/', views.PostDelete.as_view(), name='delete'),
]

