from django.urls import path
from user_auth.views import register
from user_auth.views import login_user
from user_auth.views import logout_user
from . import views 

app_name = 'user_auth'

urlpatterns = [
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),

]