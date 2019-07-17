from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll


def poll_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values('question','created_by__username', 'publish_date'))}

    return JsonResponse(data)


def poll_details(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    data = {
        "results": {
            'question': poll.question,
            'created_by__username': poll.created_by.username,
            'publish_date': poll.publish_date
        }
    }

    return JsonResponse(data)