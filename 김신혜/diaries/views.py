from django.shortcuts import render

# Create your views here.
def diary(request):
    data = request.GET.get('content')
    context = {
        'data':data
    }
    return render(request, 'diary/diary,html', context)
    