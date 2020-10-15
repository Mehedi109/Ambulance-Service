from django.urls import path
from . import views

urlpatterns = [
    
    #path('',views.HomeView.as_view(),name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('admin_register',views.admin_register,name="admin_register"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
]