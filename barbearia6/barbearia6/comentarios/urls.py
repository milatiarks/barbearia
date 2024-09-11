from django.urls import path
from . import views

urlpatterns = [
    path('feedback_list/', views.feedback_list),
    path('add_feedback/', views.add_feedback),
    path('', views.home, name='home'),
]
