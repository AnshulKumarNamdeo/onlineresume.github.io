from django.shortcuts import render

# Create your views here.
def eduview(request):
    return render(request, 'edu/education.html')