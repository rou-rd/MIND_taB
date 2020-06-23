from django.urls import path
from user_manager import views
from .views import users
from django.contrib import admin

app_name='user_manager'

urlpatterns=[
    path(r'admin/', admin.site.urls, name='admin' ),
    path('user_login/',views.user_login,name='user_login'),
    path('profile/',views.profile,name='profile'),
    path('connection/',views.formView,name='loginform'),
    path('profile/edit',views.update_profile,name='edit_profile'),
    path('register/',views.register,name='register'),

]
