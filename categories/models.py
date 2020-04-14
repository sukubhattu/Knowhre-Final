from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from requests import get
import geoip2.database
from math import sin, cos, sqrt, atan2, radians
from geopy.geocoders import Nominatim
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to='category_gallery')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Company(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "company_owner")
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='company_gallery')
    opening_hr = models.TimeField(default = '9:00')
    closing_hr = models.TimeField(default = '4:00')
    email = models.EmailField()
    #contact = models.PhoneNumberField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse('category_list')
		#if want to redirect to its detail page then
        # return reverse('company_detail' ,kwargs = {'pk' : self.pk})

    def get_distance(self):
        ip = get('https://api.ipify.org').text
        reader = geoip2.database.Reader('categories/GeoLite2-City.mmdb')
        response = reader.city(ip)
        current_lat = response.location.latitude
        current_lon = response.location.longitude
        comp_lat = self.latitude
        comp_lon = self.longitude
        R = 6373.0

        lat1 = radians(current_lat)
        lon1 = radians(current_lon)
        lat2 = radians(comp_lat)
        lon2 = radians(comp_lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c* 1000
        return(distance)
    
    def get_city(self):
        
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        comp_lat = self.latitude
        comp_lon = self.longitude
        location = geolocator.reverse("" + str(comp_lat) + ","+ str(comp_lon) + "")
        city = location.address
        return(city)


class Comment(models.Model):
    text = models.TextField(max_length = 4000)
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text