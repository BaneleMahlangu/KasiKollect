from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'interaction/home.html')

def report(request):
    return render(request, 'interaction/report.html')

def tracker(request):
    return render(request, 'interaction/tracker.html')

def schedule(request):
    return render(request, 'interaction/schedule.html')