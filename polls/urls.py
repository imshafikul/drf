from django.urls import path
from .views import poll_list, poll_details


urlpatterns = [
    path('polls', poll_list, name="poll_list"),
    path('polls/<int:pk>/', poll_details, name="poll_details")
]