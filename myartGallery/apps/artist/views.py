from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Artwork
from ..citizens.models import Order


# Create your views here.
def home(request):
    artworks = Artwork.objects.all().order_by('id')
    return render(request, 'home.html', {"artworks": artworks})


def about(request):
    return render(request, 'About.html')


def contactus(request):
    return render(request, 'contact.html')


def addArtwork(request):
    return render(request, 'addArtwork.html')


def uploadArtwork(request):
    a = Artwork()
    a.name = request.POST.get("name")
    a.artworkstyle = request.POST.get("artworkstyle")
    a.price = request.POST.get("price")
    a.deliveryCharges = request.POST.get("deliveryCharges")
    a.imagePath = request.POST.get("imagePath")
    a.description = request.POST.get("description")
    a.save()
    print('inside uploadArtwork')
    messages.success(request, f'Artwork "{a.name}" successfully uploaded')
    return redirect("/")


def editArtwork(request, id):
    print("inside edit", id)
    artwork = Artwork.objects.get(id=id)
    return render(request, 'editArtwork.html', {"artwork": artwork})


def updateArtwork(request, id):
    a = Artwork.objects.get(id=id)
    a.name = request.POST.get("name")
    a.artworkstyle = request.POST.get("artworkstyle")
    a.price = request.POST.get("price")
    a.deliveryCharges = request.POST.get("deliveryCharges")
    a.imagePath = request.POST.get("imagePath")
    a.description = request.POST.get("description")
    a.save()
    print('inside updateArtwork')
    messages.success(request, f'Artwork "{a.name}" successfully updated')
    return redirect("/")


def deleteArtwork(request, id):
    a = Artwork.objects.get(id=id)
    a.delete()
    messages.success(request, f'Artwork "{a.name}" successfully Deleted')
    return redirect("/")


def artwork_style(request):
    artworks = Artwork.objects.all().order_by('id')
    return render(request, 'Artworkstyle.html', {"artworks": artworks})


def order_list(request):
    order = Order.objects.all()
    return render(request, 'order.html', {"orders": order})


def deleteOrder(request, id):
    try:
        order = Order.objects.get(id=id)
        citizen_name = order.citizenName
        order.delete()
        messages.success(request, f'Order "{citizen_name}" successfully deleted')
    except Order.DoesNotExist:
        messages.error(request, 'Order not found')

    return redirect("order")
