from django.forms import ValidationError
import re

from myweb.api.mapping import (
    serial_number_mask_mapping,
)

def validator_serial_number_mask(value):
    """Валидатор маски серийного номера типа оборудования

    Args:
        value (_type_): Полученная маска из формы, заполненной пользователем

    Raises:
        ValidationError: Ошибка валидации
    """
    regex_serial_number_mask = re.compile(r'^[NaAXZ]+$')
    
    if not regex_serial_number_mask.match(value):
        raise ValidationError(
            f'{value} is not validation seerial number mask!'
        )
        
        
def validate_serial_number(value, serial_number_mask):
    """Валидатор серийного номера оборудования

    Args:
        value (_type_): Полученный серийный номер из формы, заполненной пользователем
        serial_number_mask (_type_): Полученная маска из формы, выбранная пользователем из базы данных

    Returns:
        _type_: Проверенный валидатором серийный номер
    """
    serial_number_code = r''
    for code in serial_number_mask:
        serial_number_code += serial_number_mask_mapping.get(code)
    regex_serial_number_mask = re.compile(serial_number_code)
    
    return regex_serial_number_mask.match(value)
    