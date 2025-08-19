from django.shortcuts import render, redirect
from .models import FormSubmission
from django.utils import timezone

def indexPageView(request): 
    return render(request, 'form/index.html')

def listFormEntries(request): 
    data = FormSubmission.objects.all()
    context = {"entries": data}
    return render(request, "form/listentries.html", context)

def addFormEntry(request):
    if request.method == 'POST': 
        new_entry = FormSubmission()
        new_entry.time = timezone.now()
        new_entry.mood = request.POST.get('mood')
        new_entry.productivity = request.POST.get('productivity')
        new_entry.accomplishment = request.POST.get('accomplishment')
        new_entry.stress = request.POST.get('stress')
        new_entry.save()
        return redirect('listentries')
    return render(request, "form/addentry.html")