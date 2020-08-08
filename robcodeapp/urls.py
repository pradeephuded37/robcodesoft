from django.urls import path
from robcodeapp import views
app_name="robcodeapp"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),

    path('services/',views.services,name="services"),

    path('home/',views.home,name="home"),

    path('aboutus/',views.aboutus,name="aboutus"),

    path('contactus/',views.contactus,name="contactus"),

]