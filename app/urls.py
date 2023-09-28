from django.urls import path
from .views import (
    profile_setting, logoutUser, home, hadith, 
    hadith_detail, search, create, 
    update, delete, register, loginpage,
    login_view,
)


urlpatterns = [
    path('', home, name='home'),
    path('hadith/', hadith, name='hadith'),
    path('hadith_detail/<str:pk>/', hadith_detail, name='hadith_detail'),
    path('search/', search, name='search'),
    path('create/', create, name='create'),
    path('update/<str:pk>/', update, name='update'),
    path('delete/<str:pk>/', delete, name='detele'),
    path('register/', register, name='register'),
    path('loginpage/', loginpage, name='loginpage'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile_setting, name='profile'),
    path('login_view/', login_view, name='login_view' )
]

