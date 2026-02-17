# clients/serializers.py
from rest_framework import serializers
from .models import Client, Document

class DocumentSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    
    class Meta:
        model = Document
        fields = ['id','client', 'document_name', 'document_type', 'expiry_date', 'status', 'created_at']

class ClientSerializer(serializers.ModelSerializer):
    license_status = serializers.ReadOnlyField()
    documents_count = serializers.ReadOnlyField()
    expiring_documents_count = serializers.ReadOnlyField()
    documents = DocumentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = [
            'id', 'company_name', 'contact_person', 'email', 'phone',
            'license_expiry_date', 'license_status', 'documents_count',
            'expiring_documents_count', 'documents', 'created_at'
        ]

class ClientListSerializer(serializers.ModelSerializer):
    license_status = serializers.ReadOnlyField()
    documents_count = serializers.ReadOnlyField()
    expiring_documents_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Client
        fields = [
            'id', 'company_name', 'contact_person', 'email', 'phone',
            'license_expiry_date', 'license_status', 'documents_count',
            'expiring_documents_count', 'created_at'
        ]
