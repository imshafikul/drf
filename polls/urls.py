from django.urls import path
# from .views import poll_list, poll_details

from rest_framework.routers import DefaultRouter

# from .apiviews import PollList, PollDetails, ChoiceList, CreateVote

from .apiviews import PollViewSet, ChoiceList, CreateVote


router = DefaultRouter()
router.register('polls', PollViewSet, base_name="polls")


urlpatterns = [
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name="create_vote")
] + router.urls