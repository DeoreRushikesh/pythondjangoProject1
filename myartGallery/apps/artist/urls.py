from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('Contactus', views.contactus, name="Contactus"),
    path('addArtwork/', views.addArtwork, name="addArtwork"),
    path('uploadArtwork/', views.uploadArtwork, name="uploadArtwork"),
    path('editArtwork/<int:id>', views.editArtwork, name="editArtwork"),
    path('updateArtwork/<int:id>', views.updateArtwork, name="updateArtwork"),
    path('deleteArtwork/<int:id>', views.deleteArtwork, name="deleteArtwork"),
    path('Artworkstyle', views.artwork_style, name="Artworkstyle"),
    path('order', views.order_list, name='order'),
    path('deleteOrder/<int:id>', views.deleteOrder, name="deleteOrder"),

]
