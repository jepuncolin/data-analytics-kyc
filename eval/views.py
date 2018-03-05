from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django import forms
from .models import KYC

class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = ['com_id', 'amt','ano', ]

def hello_world(request):
    form = KYCForm()
    return render(request, 'hello_world.html', {
        'form': form
    })