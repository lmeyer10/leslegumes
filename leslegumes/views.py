#models.py
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import *

#views

def index(request):
    latest_question = Question.objects.order_by('-pub_date')[0]
    if request.method == 'GET':
        form = SurveyForm()
    else:
        form = SurveyForm(request.POST)
        if form.is_valid():
            return render(request, 'submit-received.html', {"message": "Your vote has been received."})
    return render(request, 'index.html', {"question":latest_question})

def menu(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('menu_item', None)
        if query_name:
            results = Menu.objects.filter(menu_item__contains=query_name)
            print(results)
            return render(request, 'menu.html', {"results":results})

    return render(request, 'menu.html',)

def reviews(request):
    return render(request, 'reviews.html',)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'submit-received.html', {"message": "Thank you for reaching out. We will respond as soon as possible."})
    return render(request, 'contact.html', {"form": form})

def reserve(request):
    now = datetime.now()
    if request.method == 'GET':
        form = DateForm()
    else:
        form = DateForm(request.POST)
        if form.is_valid():
            return render(request, 'submit-received.html', {"message": "Your reservation has been received. We look forward to seeing you soon!"})
    return render(request, 'reserve.html', {"form":form})

def submitreceived(request):
    message = "Your submission has been received."
    return render(request, 'submit-received.html', {"message":message})

