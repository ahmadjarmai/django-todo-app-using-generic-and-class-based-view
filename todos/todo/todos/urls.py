from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('', views.ListViewItems.as_view(), name='list'),
    path('detail/<int:pk>/', views.DetailViewItem.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateViewItem.as_view(), name ='update'),
    path('delete/<int:pk>/', views.DeleteViewItem.as_view(), name='delete'),
    path('create/', views.CreateViewItem.as_view(), name='create'),
    path('login/', auth_views.LoginView.as_view(), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
