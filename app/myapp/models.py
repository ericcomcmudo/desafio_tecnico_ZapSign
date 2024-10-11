from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.AutoField(primary_key=True) 
    openID = models.IntegerField()
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='documents')
    externalID = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    externalID = models.CharField(max_length=255, blank=True, null=True)
    documentID = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, related_name='signers')  # Chave estrangeira

    def __str__(self):
        return self.name