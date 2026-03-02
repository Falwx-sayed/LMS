from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    status_choices = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='books',null=True, blank=True)
    photo_author = models.ImageField(upload_to='books',null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2 , null=True, blank=True)
    retal_price = models.DecimalField(max_digits=6, decimal_places=2 , null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    inavialable = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title