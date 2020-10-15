from django.urls import path
from . import views

urlpatterns = [
    path('appointment',views.appointment,name="appointment"),
    path('book',views.book,name="book")
    
]