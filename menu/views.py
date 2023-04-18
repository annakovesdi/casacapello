from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Category, Menu
from .forms import MenuForm, CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# return menu
def menu(request):
    antipasti = Menu.objects.filter(category__name__icontains='antipasti')
    primi = Menu.objects.filter(category__name__icontains='primi')
    secondi = Menu.objects.filter(category__name__icontains='secondi')
    dolci = Menu.objects.filter(category__name__icontains='dolci')

    context = {
        'antipasti': antipasti,
        'primi': primi,
        'secondi': secondi,
        'dolci': dolci,
    }
    return render(request, "menu/menu.html", context)


# menu management page
@login_required
def management(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    antipasti = Menu.objects.filter(category__name__icontains='antipasti')
    primi = Menu.objects.filter(category__name__icontains='primi')
    secondi = Menu.objects.filter(category__name__icontains='secondi')
    dolci = Menu.objects.filter(category__name__icontains='dolci')
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully added image item')
            return redirect(reverse('management'))
        else:
            messages.error(request, 'Failed to add item. Please check your input.')
    else:
        form = CategoryForm()
    form = CategoryForm

    context = {
        'antipasti': antipasti,
        'primi': primi,
        'secondi': secondi,
        'dolci': dolci,
        'form': form,
    }
    return render(request, "menu/management.html", context)


# add item
@login_required
def add_item(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully added menu item')
            return redirect(reverse('management'))
        else:
            messages.error(request, 'Failed to add item. Please check your input.')
    else:
        form = MenuForm()
    form = MenuForm
    template = 'menu/add.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# edit an item
@login_required
def edit(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    item = get_object_or_404(Menu, pk=item_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited item')
            return redirect(reverse('menu'))
        else:
            messages.error(
                request, 'Failed to edit work. Please check your input.')
    else:
        form = MenuForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'menu/edit.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


# delete item
@login_required
def delete_item(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    item = get_object_or_404(Menu, pk=menu_id)
    item.delete()
    messages.success(request, 'Succesfully deleted work')
    return redirect(reverse('management'))

