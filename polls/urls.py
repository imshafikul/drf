from django.urls import path
from .views import poll_list, poll_details

from .apiviews import PollList, PollDetails, ChoiceList, CreateVote


urlpatterns = [
    path('polls', PollList.as_view(), name="poll_list"),
    path('polls/<int:pk>/', PollDetails.as_view(), name="poll_details"),
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name="create_vote")
]