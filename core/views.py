from django.shortcuts import render

# Create your views here.
def home(request):
    context ={'context': 'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    return render(request, 'core/contact.html')

