from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render

from polls.models import Entry


def index(request):
    latest_entry_list = Entry.objects.order_by('-entry_date_date')[:5]
    context = {'latest_entry_list': latest_entry_list}
    return render(request, 'polls/index.html', context)


def entry_detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404("Entry does not exist")

    return render(request, 'polls/entry/detail.html', {'entry': entry})


def entry_results(request, entry_id):
    response = "You're looking at the results of entry %s."
    return HttpResponse(response % entry_id)


def entry_vote(request, entry_id):
    return HttpResponse("You're voting on entry %s." % entry_id)


def investment_detail(request, investment_id):
    return HttpResponse("You're looking at investment %s." % investment_id)


def investment_results(request, investment_id):
    response = "You're looking at the results of investment %s."
    return HttpResponse(response % investment_id)


def investment_vote(request, investment_id):
    return HttpResponse("You're voting on investment %s." % investment_id)
