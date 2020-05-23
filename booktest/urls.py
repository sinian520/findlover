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
    path('UploadShowlove/', views.UploadShowlove),
    path('Showlove/', views.Showlove),
    path('AddCount/', views.AddCount),
    path('Activeapply/', views.Activeapply),
    path('Showactive/', views.Showactive),
    path('AttendActive/', views.AttendActive),
    path('GetEvaluate/', views.GetEvaluate),
    path('PostEvaluate/', views.PostEvaluate),
    path('GetActiveUser/', views.GetActiveUser),
    path('HomeUser/', views.HomeUser),
    path('AddFriend/', views.AddFriend),
    path('AddUserCount/', views.AddUserCount),
    path('PostHelp/', views.PostHelp),
    path('AskHelp/', views.AskHelp),
    path('Reponseshow/', views.Reponseshow),
    path('PostReponse/', views.PostReponse),
    path('GetText/', views.GetText),
]
