from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('events/', views.events_page),
    path('add-event/', views.add_event),
    path('edit/<int:id>/', views.edit_event),
    path('delete/<int:id>/', views.delete_event),
    path('donate/', views.donate),
    path('event/<int:id>/', views.event_detail),
]