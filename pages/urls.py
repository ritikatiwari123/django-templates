from django.urls import path
from pages.views import *

urlpatterns = [ path('home/', HomePageView.as_view(), name="home-page"),
                path('about/', AboutPageView.as_view(), name="about-page"),]