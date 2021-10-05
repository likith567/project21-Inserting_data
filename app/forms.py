from django import forms
 

class studentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topicname=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField(max_length=100)