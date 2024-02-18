from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import PlaceOrderForm
from .models import Artwork


def welcome(request):
    artworks = Artwork.objects.all().order_by('id')
    return render(request, 'welcome.html', {"artworks": artworks})


def buy(request, id):
    try:
        artwork = Artwork.objects.get(id=id)
    except Artwork.DoesNotExist:
        raise Http404("Artwork does not exist")

    return render(request, 'buy.html', {"artwork": artwork})


def placeOrder(request, id):
    try:
        artwork = Artwork.objects.get(id=id)
    except Artwork.DoesNotExist:
        raise Http404("Artwork does not exist")

    if request.method == 'POST':
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.artName = artwork.name
            order.save()

            # its redirect to home page after submitting
            return redirect('home')
        else:
            # Handle form validation errors
            return render(request, 'placeOrder.html', {"artwork": artwork, "form": form})
    else:
        form = PlaceOrderForm()
    messages.success(request, f'Artwork "{artwork.name}" successfully Purchased.')

    return render(request, 'placeOrder.html', {"artwork": artwork, "form": form})


def artwork_by_artworkstyle(request, artworkstyle):
    artworks = Artwork.objects.filter(artworkstyle__iexact=artworkstyle)  # Case-insensitive matching
    return render(request, 'gallery.html', {'artworks': artworks, 'artworkstyle': artworkstyle})
