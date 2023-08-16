from django.db import models
import uuid
import datetime


# Create your models here.

class Participant(models.Model):
    qrcode_id = models.UUIDField(null=False, unique=True)
    first_name = models.CharField(null=True, max_length=100)
    name = models.CharField(null=True, max_length=100)
    phone_nr = models.CharField(null=False,unique=True,max_length=15)    
    date_entered = models.DateTimeField(auto_now=True)
    scans=models.IntegerField(default=0)
    stand1=models.BooleanField(default=False)
    stand2=models.BooleanField(default=False)
    stand3=models.BooleanField(default=False)
    stand4=models.BooleanField(default=False)
    stand5=models.BooleanField(default=False)
    stand6=models.BooleanField(default=False)
    stand7=models.BooleanField(default=False)
    stand8=models.BooleanField(default=False)
    stand9=models.BooleanField(default=False)
    stand10=models.BooleanField(default=False)
    stand11=models.BooleanField(default=False)
    stand12=models.BooleanField(default=False)
    stand13=models.BooleanField(default=False)
    stand14=models.BooleanField(default=False)
    stand15=models.BooleanField(default=False)
    stand16=models.BooleanField(default=False)
    stand17=models.BooleanField(default=False)
    stand18=models.BooleanField(default=False)
    stand19=models.BooleanField(default=False)
    stand20=models.BooleanField(default=False)
    stand21=models.BooleanField(default=False)
    stand22=models.BooleanField(default=False)
    stand23=models.BooleanField(default=False)
    stand24=models.BooleanField(default=False)
    stand25=models.BooleanField(default=False)
    stand26=models.BooleanField(default=False)
    stand27=models.BooleanField(default=False)
    stand28=models.BooleanField(default=False)
    stand29=models.BooleanField(default=False)
    stand30=models.BooleanField(default=False)
    stand31=models.BooleanField(default=False)
    stand32=models.BooleanField(default=False)

class QrCodeId(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    is_used = models.BooleanField(default=False)

class Entry(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    exit = models.BooleanField(default=False)