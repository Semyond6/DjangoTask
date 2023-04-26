from django.conf import settings
from django.urls import path


from . import views

urlpatterns = [
    path('home/', views.get_home_page, name='home'),
    path('home/equipment-type-create/', views.equipment_type_process),
    path('home/equipment/', views.equipment_process_to_api),
    path('home/equipment-type-all/', views.equipment_type_to_api, name='type-all'),
    path('home/equipment-type/all/', views.equipment_type_all_to_html),
    path('home/equipment/<id>', views.equipment_get_id, name='equipment-id'), 
    path('home/equipment/all/', views.equipment_all_to_html),
]