from django.conf.urls import url
from django.urls import path
from booktest import views
urlpatterns = [
    path('LoginView/', views.LoginView),
    path('RegisterCheck/', views.RegisterCheck),
    path('Register/', views.Register),
    path('Personal/', views.Personal),
    path('ChangePersonal/', views.ChangePersonal),
    path('Change2Personal/', views.Change2Personal),
    path('UploadPersonal/', views.UploadPersonal),
    path('Vip/', views.Vip),
    path('Bevip/', views.Bevip),
    path('GetFriends/', views.GetFriends),

]
