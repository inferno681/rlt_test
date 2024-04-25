import json
from datetime import datetime

from constants import (
    DATA_KEYS,
    INVALID_DATE,
    INVALID_GROUP_TYPE,
    INVALID_KEY,
    INVALID_STRUCTURE,
    VALID_DATE_FORMAT,
    VALID_GROUP_TYPES,
    REQUEST_KEYS,
)


def date_format_check(data, keys):
    """Функция проверки формата даты"""
    invalid_key_dates = []
    for key in keys:
        try:
            datetime.strptime(data[key], VALID_DATE_FORMAT)
        except ValueError:
            invalid_key_dates.append(key)
    if invalid_key_dates:
        return (False, INVALID_DATE.format(key_date=invalid_key_dates))
    return None


def input_check(input):
    """Функция проверки присланных данных"""
    try:
        data = json.loads(input)
    except json.JSONDecodeError:
        return (False, INVALID_STRUCTURE)
    if not isinstance(data, dict):
        return (False, INVALID_STRUCTURE)
    invalid_keys = []
    for key in data.keys():
        if key not in REQUEST_KEYS:
            invalid_keys.append(key)
    if invalid_keys:
        return (False, INVALID_KEY.format(invalid_keys=invalid_keys))
    date_format_message = date_format_check(data, DATA_KEYS)
    if date_format_message:
        return date_format_message

    if data["group_type"] not in VALID_GROUP_TYPES:
        return (False, INVALID_GROUP_TYPE.format(period=data["group_type"]))

    return (True, data)
