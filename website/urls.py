from django.urls import path
from . import views # from our website directory we can import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact.html',views.contact,name="contact"),
]
