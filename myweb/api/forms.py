from django import forms
from catalog.models import Equipment, Equipment_type

class EquipmentTypeForms(forms.ModelForm):
    """Форма для отображения/запроса данных из таблицы типа оборудования"""
    
    class Meta:
        model = Equipment_type
        fields = ['type_name', 'serial_number_mask']


class EquipmentForms(forms.ModelForm):
    """Форма для отображения/запроса данных из таблицы оборудования"""
    
    class Meta:
        model = Equipment
        fields = ['equipment_type', 'serial_number', 'comment']
        
class EquipmentFormsID(forms.Form):
    """Форма для отображения/запроса id оборудования"""
    
    id = forms.IntegerField(min_value = 1)
    
class EquipmentFormsUpdate(forms.ModelForm):
    """Форма для обновления данных из таблицы оборудования"""
    
    id = forms.IntegerField(min_value = 1)
    class Meta:
        model = Equipment
        fields = ['equipment_type', 'serial_number', 'comment']