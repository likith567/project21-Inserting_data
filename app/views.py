from django.shortcuts import render
from app.models import Topic
from django.http import HttpResponse
from app.forms import *
from app.models import *

# Create your views here.
from app.forms import *

def student(request):
    form=studentForm()
    if request.method=='POST':
        form_data=studentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'student.html',context={'form':form})

def insert_topic(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            topic=request.POST['topic_name']
            t=Topic.objects.get_or_create(topic_name=topic)[0]
            t.save()
            return HttpResponse('Data inserted Successfully')
    return render(request,'insert_topic.html',context={'form':form})

def insert_webpage(request):
    form=WebpageForm()
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            tn=request.POST['topicname']
            n=request.POST['name']
            url=request.POST['url']
            t=Topic.objects.get_or_create(topic_name=tn)[0] 
            t.save()
            w=WebpageForm.objects.get_or_create(topic_name=t,name=n,url=url)[0]
            w.save()
            return HttpResponse('Inserted Sucessfully')
    return render(request,'insert_webpage.html',context={'form':form})
