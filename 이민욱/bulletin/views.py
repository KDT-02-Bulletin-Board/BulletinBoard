from django.shortcuts import render

# Create your views here.

app_name = 'home'
def home(request):
    return render(request, 'home.html')