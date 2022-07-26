from django import forms 
from users.models import NewUser
from django.forms import ModelForm
from .models import Meetings
from django.utils.safestring import mark_safe


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    input_formats = '%H:%M:%S %Z'

    #'time': forms.TimeInput(format='%H:%M'),
"""
class MeetingsForm(forms.Form):
    MY_Field = (
        ('electronic', 'electronic'),
        ('computer', 'computer'),
        ('economic', 'economic'),
        )
    field = models.CharField(max_length=100, choices=MY_Field,default = 'choose your field')
    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField()
    zoom_url = models.URLField(max_length=200)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)
"""
class MeetingsForm(ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = Meetings
        #fields = ['topic','title','zoom_url','zoom_password','about_meeting','date','time']
        fields = ['title','about_meeting','date','time','zoom_url','zoom_password']
        widgets = {
            'date': DateInput(attrs={'class': 'form-control mt-3 mb-3 '}),
            'time':TimeInput(attrs={'class': 'form-control mt-3 mb-3'}),
            'title': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3 '}),
            'about_meeting': forms.Textarea(attrs={'class': 'form-control mt-3 mb-3'}),
            'zoom_url': forms.URLInput(attrs={'class': 'form-control mt-3 mb-3 '}),
            'zoom_password': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3 '})


            }

        labels = {

            "about_meeting": "About the meeting:",
            "title": "Meeting title:",
            "date": "Meeting date:",
            "time": "Meeting time:",
            "zoom_url": "Meeting Zoom url:",
            "zoom_password": "Meeting Zoom password:"
        }
      


