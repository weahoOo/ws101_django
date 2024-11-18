from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from .forms import CatForm

# List all cats
def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'cats/cat_list.html', {'cats': cats})

# Add a new cat
def cat_add(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm()
    return render(request, 'cats/cat_form.html', {'form': form})

# Edit a cat
def cat_edit(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)
    return render(request, 'cats/cat_form.html', {'form': form})

# Delete a cat
def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('cat_list')
    return render(request, 'cats/cat_confirm_delete.html', {'cat': cat})

def cat_list(request):
    cats = Cat.objects.all().order_by('-id')  # Latest cats appear first
    return render(request, 'cats/cat_list.html', {'cats': cats})
