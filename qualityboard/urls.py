from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "qualityboard"

urlpatterns = [
    path('', views.index,name="landingpage"),
    path('dp', views.index,name="index"),
    path('dpm', views.dpm,name="dpm"),
    path('mob', views.mob,name="mob"),
    path('custom', views.custom,name="custom"),
    path('eda', views.eda,name="eda"),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),

]