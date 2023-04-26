from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from myweb.api.forms import EquipmentTypeForms, EquipmentForms, EquipmentFormsID, EquipmentFormsUpdate
from catalog.models import Equipment, Equipment_type
from myweb.api.validators import validate_serial_number

def get_home_page(request: Request):
    """_summary_

    Args:
        request (Request): запрос для home

    Returns:
        _type_: _description_
    """
    
    if request.method == 'GET':
        equipment_type_form = EquipmentTypeForms()
        equipment_form = EquipmentForms()
        equipment_form_id = EquipmentFormsID()
        equipment_form_update = EquipmentFormsUpdate()
        
        context = {
            'form_equipment_type_form': equipment_type_form,
            'form_equipment_form': equipment_form,
            'form_equipment_form_id': equipment_form_id,
            'form_equipment_form_update': equipment_form_update
        }
    return render(request, 'home.html', context)

def equipment_type_process(request: Request):
    """Процесс обработки запроса для типа оборудования.

    Args:
        request (Request): запрос для обработки данных типа оборудования

    Returns:
        HttpResponse: Результат выполнения запроса
    """
    result: str = ''
    if request.method == "POST":
        f = EquipmentTypeForms(request.POST)
        f.save()
        result = f'Тип оборудования сохранен!'
    
    return HttpResponse(result)

def equipment_process(request):
    """Процесс обработки запроса

    Args:
        request (_type_): запрос для обработки данных оборудования

    Returns:
        _type_: Сообщение или список объектов
    """
    result: str = ''
    if request.method == "POST":
        f = EquipmentForms(request.POST)
        g_type = Equipment_type.objects.get(id = f.data['equipment_type']).serial_number_mask
        if validate_serial_number(
            f.data['serial_number'], 
            g_type
        ):
            f.save()
            result = 'Тип оборудования сохранен!'
        else:
            result = 'Ошибка валидации!'
        
    if request.method == "GET":
        result: str = ''
        try:
            queryset = Equipment.objects.all()
        except Exception:
            result = f'Нет типов оборудования!'
        else:
            result = queryset.values('id', 
                        'equipment_type',
                        'serial_number',
                        'comment')
    return result

def equipment_type_get_all(request):
    """Метод получения списка типов оборудования

    Args:
        request (_type_): запрос для обработки данных оборудования

    Returns:
        _type_: Спискок типов оборудования
    """
    if request.method == "GET":
        result: str = ''
        try:
            queryset = Equipment_type.objects.all()
        except Exception:
            result = f'Нет типов оборудования!'
        else:
            result = queryset\
                .values('id', 
                        'type_name',
                        'serial_number_mask',
                       )
  
    return result

def equipment_get_id(request, id):
    """Метод получения оборудования по id, обновление оборудования, удаления оборудования

    Args:
        request (_type_): запрос для обработки данных оборудования

    Returns:
        _type_: Искомое оборудование, сообщение о обновлении/удалении
    """
    if request.method == "GET":
        try:
            if id != 'id':
                pk_int = int(id)
            elif id == 'id':
                pk_int = int(request.GET['id'])
            queryset = Equipment.objects.get(pk = pk_int)
        except Exception:
            result = f'Нет типов оборудования!'
        else:
            result = [{'id': queryset.id, 
                    'equipment_type': queryset.equipment_type,
                    'serial_number': queryset.serial_number,
                    'comment': queryset.comment}]
                       
            
    if request.method == "PUT" or request.method == "POST":
        pk_int = ''
        if request.POST['_method'] == "PUT":
            id_put = request.POST['id']
            serial_number = request.POST['serial_number']
            comment = request.POST['comment']
        elif request.method == "PUT":
            id_put = request.PUT['id']
            serial_number = request.PUT['serial_number']
            comment = request.PUT['comment']
        try:
            if id != 'id':
                pk_int = int(id)
            elif id == 'id':
                pk_int = int(id_put)
            dat = Equipment.objects.get(pk = pk_int)
        except Exception:
            result = f'Нет оборудования!'
        else:
            dat = Equipment.objects.filter(pk = pk_int).update(serial_number = serial_number, 
                                                               comment = comment)
            result = f'Оборудование обновлено!'
        
    if request.method == "DELETE" or request.method == "POST":
        pk_int = ''
        try:
            if id != 'id':
                pk_int = int(id)
            elif id == 'id':
                if request.method == "DELETE":
                    pk_int = int(request.DELETE['id'])     
                elif request.POST['_method'] == "DELETE":
                    pk_int = int(request.POST['id'])
            dat = Equipment.objects.get(pk = pk_int)
        except Exception:
            result = f'Нет оборудования!'
        else:
            dat = Equipment.objects.filter(pk = pk_int).delete()
            result = f'Оборудование удалено!'
        
    return HttpResponse(result, id)

def equipment_process_to_api(request):
    """Вспомогательный метод для возвращения ответа по api

    Args:
        request (_type_): запрос

    Returns:
        _type_: Сообщение или список объектов
    """
    result = equipment_process(request)
    return HttpResponse(result)

def equipment_all_to_html(request):
    """Вспомогательный метод для возвращения ответа в html шаблон

    Args:
        request (_type_): запрос

    Returns:
        _type_: Сообщение или список объектов, пагинация
    """
    result = equipment_process(request)
    
    contact_list = Equipment.objects.all()
    paginator = Paginator(contact_list, 25) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'equipment': result, 'page_obj': page_obj}
    return render(request, 'list_all.html', context)

def equipment_type_to_api(request):
    """Вспомогательный метод для возвращения ответа по api

    Args:
        request (_type_): запрос

    Returns:
        _type_: Сообщение или список объектов
    """
    result = equipment_type_get_all(request)
    return HttpResponse(result)

def equipment_type_all_to_html(request):
    """Вспомогательный метод для возвращения ответа в html шаблон

    Args:
        request (_type_): запрос

    Returns:
        _type_: Сообщение или список объектов, пагинация
    """
    result = equipment_type_get_all(request)
    
    contact_list = Equipment_type.objects.all()
    paginator = Paginator(contact_list, 25) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'equipment_type': result, 'page_obj': page_obj}
    return render(request, 'list_type_all.html', context)