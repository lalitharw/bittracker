from django.urls import path
from . import views

urlpatterns = [
    path('',views.SignUp,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout_page,name='logout')
]