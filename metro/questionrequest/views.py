from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.db.models import Q
from django.http import JsonResponse
import json
@login_required(login_url="/auth/login")
def map(request):
    return render(request, 'index.html', context = {'stat' : json.dumps(list_(request.user))})

@login_required(login_url="/auth/login")
def play(request):
    return render(request, 'map.html', context = {'stat' : json.dumps(list_(request.user))})



from django.shortcuts import render
from .models import *
from django.http import JsonResponse
def tojson(user, stat):
    d = {'moscow' : {}}
    elem = [Question.objects.get(station=stat, who=user)]
    d['moscow'][elem[0].station] = []
    for question in elem:
        ans = ''
        try:
            ans = Answer.objects.get(question=question, author=user).text
        except:
            pass
        d["moscow"][elem[0].station] = {'text' : question.text, 'ans' : ans, 'id' : question.id}
    return d


def list_(user):
    if user.is_superuser:
        return [[bool(Answer.objects.filter(question=i)), i.station] for i in Question.objects.all()]
    return [[bool(Answer.objects.filter(question=i)), i.station] for i in Question.objects.filter(who=user)]

def index(request, stat):
    return JsonResponse(tojson(request.user, stat))

def ask(request):
    return JsonResponse({"ans" : list_(request.user)})

def ans(request):
    ans = dict(request.POST)['ans'][0]
    question = dict(request.POST)['q'][0]
    anss = Answer(text=ans, author=request.user, question=Question.objects.get(id=int(question)))
    try:
        anss = Answer.objects.get(author=request.user, question=Question.objects.get(id=int(question)))
    except:
        pass
    anss.text = ans
    anss.save()
    return JsonResponse({'status' : "ok"})

def ans_play(request):
    ans = dict(request.POST)['ans'][0]
    question = dict(request.POST)['q'][0]
    anss = Answer(text=ans, question=Question.objects.get(id=int(question)))
    try:
        anss = Answer.objects.get(question=Question.objects.get(id=int(question)))
    except:
        pass
    anss.text = ans
    anss.save()
    return JsonResponse({'status' : "ok"})
