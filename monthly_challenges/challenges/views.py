from django.http import response
from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

monthly_challenges = {
  'january': 'Eat no meat for the entire month',
  'february': 'Walk for 20 min everyday',
  'march': 'do whatever you want',
  'april': 'do whatever you want',
  'may': 'Walk for 20 min everyday',
  'june': 'Eat no meat for the entire month',
  'july': 'Walk for 20 min everyday',
  'august': 'Walk for 20 min everyday',
  'september': 'Walk for 20 min everyday',
  'october': 'Walk for 20 min everyday',
  'november': 'Walk for 20 min everyday',
  'december': None,
}

def list_of_months(request):
  return render(request, 'challenges/index.html', {
    "months": list(monthly_challenges.keys())
  })

def january(request):
  return HttpResponse("This works")

def february(request):
  return HttpResponse("Walk 20 mins every day")

def monthly_challenges_by_number(request, month):
  try:
    redirect_month = list(monthly_challenges.keys())[month - 1] # .keys returns an object that looks like a list wrap it in list def to make it a propr list
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
  except:
    return HttpResponseNotFound('invalid number')

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
      "text": challenge_text,
      "month_name": month
    })
  except:
    raise Http404()