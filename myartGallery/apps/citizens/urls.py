from django.urls import path

from . import views

urlpatterns = [
    # path('buy_now/', views.buy_now, name='buy_now'),
    path('welcome/', views.welcome, name="welcome"),
    path('buy/<int:id>', views.buy, name='buy'),
    path('placeOrder/<int:id>', views.placeOrder, name='placeOrder'),
    path('gallery/<str:artworkstyle>/', views.artwork_by_artworkstyle, name='artwork_by_artworkstyle'),


]
