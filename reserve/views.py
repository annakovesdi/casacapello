from django.shortcuts import render
from .models import Reservation, BannerImage, Reservation_Date
from .forms import ReservationForm, BannerImageForm


# return reserve page
def reserve(request):
    bannerimage = BannerImage.objects.all()
    full = Reservation_Date.objects.filter(is_full=True)
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            datetime = data['date']
            email_address = data['email_address']
            message1 = (
                "Reservering by Casa Capello",
                f"Bedankt voor de reservatie voor {datetime}. Mocht er onverwachts iets tussen komen, stuur ons een mail of bel even op 070 000000. Tot binnenkort! Casa Capello",
                "None",
                [f"{email_address}"],
                )
            message2 = (
                f"Reservation {datetime}",
                f"A reservation was made. Here are the details {data}",
                "None",
                ["second@test.com"],
                )
            send_mass_mail((message1, message2), fail_silently=False)
            messages.success(request, 'Succesfully reserved')
            return redirect(reverse('menu'))
        else:
            messages.error(request, 'Failed to add item. Please check your input.')
    else:
        form = ReservationForm()
    form = ReservationForm()

    context = {
        'form': form,
        'bannerimage': bannerimage,
        'full': full,
    }
    return render(request, "reserve/reserve.html", context)


def view_reservations(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations,
    }
    return render(request, "reserve/reserve.html", context)


def test(request):
    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, "reserve/test.html", context)