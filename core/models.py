from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    class RestaurantTypeChoices(models.TextChoices):
        INDIAN = 'IN','INDIAN'
        CHINESE = 'CH','CHINESE'
        MEXICAN = 'MX','MEXICAN'
        JAPANESE = 'JP','JAPANESE'
        ARABIC = 'AR','ARABIC'
        SOMALI = 'SM','SOMALI'
        OTHER = 'NA','OTHER'
        
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    town = models.CharField(max_length=50)
    address_description = models.TextField()
    restaurant_type = models.CharField(max_length=2, choices=RestaurantTypeChoices.choices,default=RestaurantTypeChoices.OTHER)
    date_opened = models.DateField()
    longitude = models.FloatField()
    latitude =  models.FloatField()
    
    def __str__(self):
        return self.name
    
    
class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"Rating: %d" % self.rating
    

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    yearly_income = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()