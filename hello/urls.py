# The urls.py file is where you specify patterns to route different URLs to their appropriate views.
from django.urls import path
from hello import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("contact/", views.contact, name="contact"),
  path("hello/<name>", views.hello_there, name="hello_there")
]