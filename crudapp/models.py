from datetime import date
from django.db import models
from django.utils import timezone

class citizen(models.Model):

    id = models.AutoField(primary_key=True)
    citizen_id = models.CharField("citizen_id", max_length=30, blank = True, null = True)

    preName = models.CharField("preName", max_length=10, blank = True, null = True)
    firstName = models.CharField("firstName", max_length=30, blank = True, null = True)
    lastName = models.CharField("lastName", max_length=30, blank = True, null = True)
    sex = models.CharField("sex", max_length=10, blank = True, null = True)
    phone = models.CharField("phone",max_length=20, blank = True, null = True)

    origin_tambon = models.CharField("origin_tambon", max_length=50, blank = True, null = True)
    origin_distrinct = models.CharField("origin_distrinct", max_length=50, blank = True, null = True)
    origin_province = models.CharField("origin_province", max_length=50, blank = True, null = True) 
    
    vehicle = models.CharField("vehicle", max_length=20, blank = True, null = True) 
    dates_at = models.DateTimeField("dates_at", auto_now_add=True)

    is_foreigner = models.CharField("is_foreigner", max_length=10, blank = True, null = True) #ชาวต่างชาติ=1,ชาวไทย=0
    country = models.CharField("country", max_length=50, blank = True, null = True)  #default=thai
    citizen_img = models.FileField(upload_to='images/', null=True, verbose_name="")
    destination_tambon = models.CharField("destination_tambon", max_length=50, blank = True, null = True)
    destination_distrinct = models.CharField("destination_distrinct", max_length=50, blank = True, null = True)
    destination_province = models.CharField("destination_province", max_length=50, blank = True, null = True) 
 
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("created_at", auto_now_add=True)
    class Meta:  
        db_table = "citizens"  

    

    def __str__(self):
        return self.firstName



