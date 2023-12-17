
from django.urls import path
from . import views
from car.views import DetailCarView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('details/<int:carid>/', DetailCarView.as_view(), name='details_profile'),
    
]
