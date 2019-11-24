from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="shop"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker/', views.tracker,name="Tracker"),
    path('productview/', views.prodView,name="prodView"),
    path('search/', views.search,name="search"),
    path('checkout/', views.checkout,name="checkout"),

    

]

