from django.urls import path
from .views import poll_list, poll_details

from .apiviews import PollList, PollDetails


urlpatterns = [
    path('polls', PollList.as_view(), name="poll_list"),
    path('polls/<int:pk>/', PollDetails.as_view(), name="poll_details")
]