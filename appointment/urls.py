from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email),
    path('login/', views.login_page, name='professor_login'),
    path('booking/', views.booking_page),
    path('main/', views.main_page),
    path('professor/', views.professor_page, name='professor')
]