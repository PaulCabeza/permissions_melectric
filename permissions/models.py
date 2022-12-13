from django.db import models

# Create your models here.

# class State(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name    

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # state = models.ForeignKey(State, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class  Meta:
        verbose_name_plural  =  "Cities"

class Registration(models.Model):
    registration_number = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    issued_date = models.DateField()
    issued_by = models.CharField(max_length=100)
    expiration_date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_number

class Permission(models.Model):
    permission_number = models.CharField(max_length=100)
    po = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    permission_document = models.FileField(upload_to='files', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.permission_number