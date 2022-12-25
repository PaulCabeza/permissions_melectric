from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseOrder(models.Model):
    STATUS = (
    ("PENDING", "Pending"),
    ("PROGRESS", "In Progress"),
    ("CLOSED", "Closed"),    
    ("DONE", "Done")
    )
    number = models.CharField(max_length=25, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")    
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

