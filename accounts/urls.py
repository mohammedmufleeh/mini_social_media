from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home,name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('photos/<int:pk>/comment/', views.add_comment, name='add_comment'),
]
