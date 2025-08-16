from django.shortcuts import render
from .views import addFormEntry

# Create your views here.
def addFormEntry(request):
    return render(request, "form/addentry.html")