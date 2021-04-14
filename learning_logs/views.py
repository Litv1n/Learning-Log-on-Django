from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required

def index(request):
    """ Home page in app Learning Log """
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """ output all topics """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # check if user is topic owner
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ define new topic """
    if request.method != 'POST':
        # not send data, create empty form
        form = TopicForm()
    else:
        # send POST data,  handle data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)  # Save topic in a variable.
            new_topic.owner = request.user  # Set topics owner attribute to current user.
            new_topic.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Add new post about specific topic """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # data do not send; create empty form
        form = EntryForm()
    else:
        # POST data sent; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ edit existing entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Original request; the form is filled with the data of the current record.
        form = EntryForm(instance=entry)
    else:
        # send data POST; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry' : entry, 'topic' : topic, 'form' : form}
    return render(request, 'learning_logs/edit_entry.html', context)