from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_list, name='business_list'),
    path('business/new/', views.create_business, name='business_create'),
    path('business/edit/<int:business_id>', views.edit_business, name='business_edit'),
    path('business/get/<int:business_id>', views.get_business, name='business_get'),
    path('business/del/<int:business_id>', views.delete_business, name='business_delete'),

]
