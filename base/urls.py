from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('addTask/', views.addTask, name='addTask'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('completeTask/<int:pk>/', views.completeTask, name='completeTask'),
    path('uncompleteTask/<int:pk>/', views.uncompleteTask, name='uncompleteTask'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

]