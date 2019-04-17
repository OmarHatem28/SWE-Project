from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:company_id>/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommendUsers/', views.recommendUsers, name='recommendUsers'),
]
