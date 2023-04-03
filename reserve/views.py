from django.shortcuts import render
from .models import Reserve


# return reserve page
def reserve(request):
    reserve = Reserve.objects.all()
    context = {
        'reserve': reserve,
    }
    return render(request, "reserve/reserve.html", context)

