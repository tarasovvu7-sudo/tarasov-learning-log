from django import forms
from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": "Topic name"}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Notes"}
        widgets = {"text": forms.Textarea(attrs={"rows": 6})}