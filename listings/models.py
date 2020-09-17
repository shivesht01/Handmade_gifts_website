from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor=models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    size=models.IntegerField()
    bathroom=models.DecimalField(max_digits=2, decimal_places=1)
    lot_size=models.DecimalField(max_digits=5, decimal_places=1)
    garage=models.IntegerField()
    main_image=models.ImageField(upload_to='photos/%Y/%m/%d/')
    aux_image_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    aux_image_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    aux_image_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    aux_image_4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    aux_image_5=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published=models.BooleanField(default=True)
    listing_date=models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title


    
    


