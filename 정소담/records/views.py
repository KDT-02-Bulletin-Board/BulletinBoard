from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Record

# Create your views here.

def record(request, year=None, month=None):
    records = Record.objects.order_by('record_date')
    year = request.GET.get('year')
    month = request.GET.get('month')

    if year and month:
        records = records.filter(record_date__year=year, record_date__month=month)

    context = {
        'records' : records,
        'years' : range(2020,2024),
        'months' : range(1,13),
    }


    return render(request, 'records/record.html', context)  

def diary(request, pk):
    record = Record.objects.get(pk=pk)
    context = {
        'record' : record,
    }
    return render(request,'records/diary.html', context)

def write(request):
    return render(request, 'records/write.html')

def success(request):
    title = request.POST['title']
    record_date = request.POST['record_date']
    imgfile = request.FILES.get('imgfile')
    content = request.POST['content']

    record = Record(title = title, record_date=record_date, imgfile=imgfile, content = content)
    record.save()
    
    return redirect("records:diary", record.pk)

def delete(request, pk):
    record = Record.objects.get(pk=pk)
    record.delete()

    return redirect("records:record")

def edit(request, pk):
    record = Record.objects.get(pk=pk)
    context = {
        'record' : record,
    }

    return render(request,'records/edit.html',context)

def update(request,pk):
    record = get_object_or_404(Record, pk=pk)

    if request.method == 'POST':
        if request.FILES.get('imgfile'):
            record.imgfile = request.FILES['imgfile']

        record.title = request.POST.get('title')
        record.record_date = request.POST.get('record_date')
        record.content = request.POST.get('content')
        record.save()

        return redirect('records:diary', record.pk)
    else:
        return render(request, 'edit.html', {'record': record})
