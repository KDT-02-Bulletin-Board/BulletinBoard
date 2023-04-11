from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Diary
from .forms import DiaryForm
from django.contrib import messages
from datetime import date

# Create your views here.

# @login_required
# def diary_list_by_year(request, year):
#     diaries = Diary.objects.filter(date__year=year)
#     context = {'diaries': diaries}
#     return render(request, 'diary.html', context)

# @login_required
# def diary_list_by_month(request, year, month):
#     diaries = Diary.objects.filter(date__year=year, date__month=month)
#     context = {'diaries': diaries}
#     return render(request, 'diary.html', context)

# @login_required
# def diary_list_by_day(request, year, month, day):
#     diaries = Diary.objects.filter(date__year=year, date__month=month, date__day=day)
#     context = {'diaries': diaries}
#     return render(request, 'diary.html', context)

def diary(request):
    if request.method == 'POST':
        year = request.POST.get('year', date.today().year)
        month = request.POST.get('month', date.today().month)
        day = request.POST.get('day', date.today().day)
        diaries = Diary.objects.order_by('record_date').filter(record_date__year=year, record_date__month=month, record_date__day=day)
        context = {
            'diaries': diaries,
            'years' : range(2020,2024),
            'months' : range(1,13),
            'days' : range(1,32),
        }
        return render(request, 'diaries/diary.html', context)
    else:
        diaries = Diary.objects.order_by('record_date')
        context = {
            'diaries': diaries,
            'years' : range(2020,2024),
            'months' : range(1,13),
            'days' : range(1,32),
        }
        return render(request, 'diaries/diary.html', context)


def diarypage(request, pk):
    diary = Diary.objects.get(pk=pk)
    context = {
        'diary' : diary,
    }
    return render(request,'diaries/diarypage.html', context)


def write(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:diarypage', diary.pk)
    else:
        form = DiaryForm()
    context = {
        'form' : form,
    }
    return render(request, 'diaries/write.html', context)


def delete(request, pk):
    diary = Diary.objects.get(pk=pk)
    diary.delete()
    return redirect("diaries:diary")


def edit(request, pk):
    if request.method == 'POST':
        diary = Diary.objects.get(pk=pk)
        form = DiaryForm(request.POST, request.FILES, instance=diary)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:diarypage', diary.pk)
    else:
        diary = Diary.objects.get(pk=pk)
        form = DiaryForm(instance=diary)
    context = {
        'diary': diary,
        'form' : form,
    }
    return render(request, 'diaries/edit.html', context)

def calendar(request):
    diaries = Diary.objects.order_by('record_date')
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:diarypage', diary.pk)
    else:
        form = DiaryForm()
    context = {
        'form' : form,
        'diaries': diaries,
    }
    return render(request,'diaries/calendar.html', context)