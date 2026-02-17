from django.urls import path
from . import views
urlpatterns = [
        path('clients/', views.client_list_create, name='client-list-create'),
            path('clients/<int:pk>/', views.client_detail, name='client-detail'),
                path('clients/<int:client_id>/documents/', views.client_documents, name='client-documents'),
]