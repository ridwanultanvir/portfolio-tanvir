from django.shortcuts import render
from .models import Job

# Create your views here.


def showJobs(request):
    jobs = Job.objects
    return render(request, 'jobs.html', {'jobs': jobs})
