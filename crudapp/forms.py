from django import forms
from .models import citizen
from datetime import date

class CitizenForm(forms.ModelForm):
    class Meta:
        model = citizen
        citizen_id = forms.CharField(label='citizen_id', max_length=100)
        firstName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        lastName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
        CHOICES = [('M','Male'),('F','Female')]
        #sex=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
        citizen_img = forms.FileField(label='Select a file',help_text='max. 42 megabytes')
        FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
        sex= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
        #dates_at = forms.CharField(label='dates_at', max_length=100)
        #subject_type = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=Subject_type.objects.all(), label='')
        fields = "__all__"  