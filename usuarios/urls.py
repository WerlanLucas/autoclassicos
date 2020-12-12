from django.urls import path
from django.contrib.auth import views as auth_view
from .views import criar_usuario

urlpatterns=[
path('login/', auth_view.LoginView.as_view(

	template_name ='usuarios/form_login.html'), 
	name='login'),

path('logout/', auth_view.LogoutView.as_view(), 
	name='logout'),

path('criar_usuario/', criar_usuario, name='criar_usuario'), 



]