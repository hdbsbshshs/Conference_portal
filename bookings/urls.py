from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list_view, name='booking_list'),
    path('new/', views.booking_form_view, name='booking_form'),
    path('admin/', views.admin_dashboard_view, name='admin_dashboard'),
]

