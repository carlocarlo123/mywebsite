from django.urls import path
from . import views # from our website directory we can import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('service.html',views.service,name="service"),
    path('pricing.html',views.pricing,name="pricing"),
    path('blog.html',views.blog,name="blog"),
    path('blog_details.html',views.blog_details,name="blog_details"),
]
