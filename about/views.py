from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import About
from .forms import AboutForm
from django.contrib.auth.decorators import login_required


# return homepage
def about(request):
    about = About.objects.all()
    context = {
        'about': about,
    }
    return render(request, "about/about.html", context)


@login_required
def edit_about(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only an Admin can access this page')
        return redirect(reverse('about'))
    existing_item = About.objects.first()
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=existing_item)
        if form.is_valid():
            existing_item.delete()
            form.save()
            messages.success(request, 'Succesfully saved')
            return redirect(reverse('about'))
        else:
            messages.error(
                request, 'Failed to add item. Please check your input.')
    else:
        form = AboutForm(instance=existing_item)
    form = AboutForm(instance=existing_item)
    template = 'about/edit_about.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

