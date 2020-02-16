from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import ListForm
from .models import List


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all().order_by('completed')
            messages.success(request, 'Item Has Been Added To List!')
            return render(request, 'home.html', {'all_items': all_items})
        messages.error(request, 'Nothing to add')
        return redirect('home')

    else:
        all_items = List.objects.all().order_by('completed')
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    context = {'first_name': 'Bob', 'last_name': 'D'}
    return render(request, 'about.html', context)


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item Has Been Deleted!')
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item Has Been Edited!')
            return redirect('home')
        messages.error(request, 'Invalid value!')
        return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


def version(request):
    return JsonResponse({"version": 3.14})
