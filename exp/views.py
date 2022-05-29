from django.shortcuts import render

# Create your views here.
def WorkExp(request):
    return render(request, 'exp/experience.html')