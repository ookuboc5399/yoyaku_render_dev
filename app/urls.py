from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('camp/', views.CampView.as_view(), name='camp'),
    path('', views.StoreView.as_view(), name='store'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('store/<int:pk>/', views.StaffView.as_view(), name='staff'),
]