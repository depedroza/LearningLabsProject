from cgitb import html
import re
from django.shortcuts import render, redirect
from .forms import TopicForm

from .models import Topic

# Create your views here.


def index(request):
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.all()

    context = {"topics": topics}
    # key is what you have to refer to in html: value is whatever you called it in view (line 13)

    return render(request, "MainApp/topics.html", context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()

    context = {"topic": topic, "entries": entries}

    return render(request, "MainApp/topic.html", context)


def new_topic(request):
    if request.method != "POST":
        form = TopicForm()

    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect("MainApp:topics")

    context = {"form": form}
    return render(request, "MainApp/new_topic.html", context)
