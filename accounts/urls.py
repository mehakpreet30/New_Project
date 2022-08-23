from .views import RegisterAPI, StaffAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from . import views


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    #path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/staff/', StaffAPI.as_view(), name='staff'),
    path('', views.ApiOverview, name='home'),
    path('api/all/', views.view_items, name='view_items'),
    path('api/create/', views.add_items, name='add-items'),
    path('api/staff/<str:id>/update', views.update_items, name='update-items'),
    path('api/staff/delete/<str:id>/', views.delete_items, name='delete-items'),


]
