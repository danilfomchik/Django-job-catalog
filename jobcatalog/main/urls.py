from django.urls import path
from . import views

# управление юрл адресом сайта
urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('create-job', views.create, name="create"),
    path('view-job/<str:pk>/', views.view, name="view"),
    path('update-job/<str:pk>/', views.update, name="update"),
    path('delete-job/<str:pk>/', views.delete, name="delete"),
]
