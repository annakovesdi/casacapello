from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Category, Wines, BannerImage
from .forms import WinesForm, BannerImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# return menu
def wines(request):
    bannerimage = BannerImage.objects.all()
    bianchi = Wines.objects.filter(category__name__icontains='bianchi')
    rossi = Wines.objects.filter(category__name__icontains='rossi')
    spumanti = Wines.objects.filter(category__name__icontains='spumanti')

    context = {
        'bannerimage': bannerimage,
        'bianchi': bianchi,
        'rossi': rossi,
        'spumanti': spumanti,
    }
    return render(request, "wines/wines.html", context)


# menu management page
@login_required
def wine_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    bianchi = Wines.objects.filter(category__name__icontains='bianchi')
    rossi = Wines.objects.filter(category__name__icontains='rossi')
    spumanti = Wines.objects.filter(category__name__icontains='spumanti')
    existing_item = BannerImage.objects.all()
    if request.method == 'POST':
        form = BannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            if existing_item:
                existing_item.delete()
            form.save()
            messages.success(request, 'Succesfully added image item')
            return redirect(reverse('wine_management'))
        else:
            messages.error(request, 'Failed to add item. Please check your input.')
    else:
        form = BannerImageForm()
    form = BannerImageForm

    context = {
        'bianchi': bianchi,
        'rossi': rossi,
        'spumanti': spumanti,
        'form': form,
    }
    return render(request, "wines/wine_management.html", context)


# add item
@login_required
def add_wine(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = WinesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully added wine')
            return redirect(reverse('management'))
        else:
            messages.error(request, 'Failed to add item. Please check your input.')
    else:
        form = WinesForm()
    form = WinesForm
    template = 'wines/add_wine.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# edit an item
@login_required
def edit_wine(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    item = get_object_or_404(Wines, pk=item_id)
    if request.method == 'POST':
        form = WinesForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited item')
            return redirect(reverse('wine_management'))
        else:
            messages.error(
                request, 'Failed to edit work. Please check your input.')
    else:
        form = WinesForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'wines/edit_wine.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


# delete item
@login_required
def delete_wine(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('home'))
    item = get_object_or_404(Wines, pk=wines_id)
    item.delete()
    messages.success(request, 'Succesfully deleted work')
    return redirect(reverse('wine_management'))


