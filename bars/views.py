from django.shortcuts import render, redirect, get_object_or_404
from .models import Recurt, Task, ShadowHand
from .forms import RecurtForm, SithForm, ShadowHandForm

def base(request):
    return render (request, 'main.html')

def task(request):
	task = Task.objects.all()
	return render(request, 'task.html', {'task': task})

def recurt_form(request):
    if request.method == "POST":
        form = RecurtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recurt_info')
    else:
        form = RecurtForm()
        return render(request, 'recurt_form.html', {'form': form})

def recurt(request):
    recurt = Recurt.objects.all()
    return render(request, 'recurt_info.html', {'recurt': recurt})

def sith_form(request):
    if request.method == "POST":
        form = SithForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recurt_info')
    else:
        form = SithForm()
        return render(request, 'sith_form.html', {'form': form})

def shadow_hand(request):
    shadowhand = ShadowHand.objects.all()
    return render(request, 'shadowhand_info.html', {'shadowhand': shadowhand})

def shadowhand_form(request):
    if request.method == "POST":
        form = ShadowHandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shadowhand_info')
    else:
        form = ShadowHandForm()
        return render(request, 'shadowhand_form.html', {'form': form})
