from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Eligibility


# Create your views here.
class EligibilityCreateView(CreateView):
    model = Eligibility

    fields = ['date' ,'area', 'mobile_number', 'address', 'age', 'comments']
