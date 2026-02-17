# clients/models.py
from django.db import models
from datetime import datetime, timedelta

class Client(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    license_expiry_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    @property
    def license_status(self):
        if not self.license_expiry_date:
            return 'No Date'
        
        today = datetime.now().date()
        days_diff = (self.license_expiry_date - today).days
        
        if days_diff < 0:
            return 'Expired'
        elif days_diff <= 30:
            return 'Expiring Soon'
        else:
            return 'Active'

    @property
    def documents_count(self):
        return self.documents.count()

    @property
    def expiring_documents_count(self):
        today = datetime.now().date()
        thirty_days = today + timedelta(days=30)
        return self.documents.filter(
            expiry_date__lte=thirty_days,
            expiry_date__gte=today
        ).count()

class Document(models.Model):
    DOCUMENT_TYPES = [
        ('Trade License', 'Trade License'),
        ('MOA', 'MOA'),
        ('Passport', 'Passport'),
        ('Visa', 'Visa'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    expiry_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_name} - {self.client.company_name}"

    @property
    def status(self):
        if not self.expiry_date:
            return 'No Date'
        
        today = datetime.now().date()
        days_diff = (self.expiry_date - today).days
        
        if days_diff < 0:
            return 'Expired'
        elif days_diff <= 30:
            return 'Expiring Soon'
        else:
            return 'Active'
