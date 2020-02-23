from django.conf.urls import url
from django.urls import path
from booktest import views
urlpatterns = [
    path('LoginView/', views.LoginView),
    path('RegisterCheck/', views.RegisterCheck),
    path('Register/', views.Register),
]
