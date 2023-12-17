
from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:carid>/', views.DetailCarView.as_view(), name='car_details'),
    path('buynow/<int:carid>/', views.buy_now, name='buynow'),
]
