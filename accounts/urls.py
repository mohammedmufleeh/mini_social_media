from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home,name='home'),
    path('upload/', views.upload_image, name='upload_image'),
]
