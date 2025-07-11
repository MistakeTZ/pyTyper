import builtins
import importlib

def get_attributes(name: str):
    parts = name.split('.')
    
    # Попробуем найти первый элемент: встроенные, globals, locals
    base_name = parts[0]
    
    # 1. Попробуй найти в builtins (например: int, str)
    obj = getattr(builtins, base_name, None)

    # 2. Попробуй найти в globals/locals
    if obj is None:
        obj = globals().get(base_name) or locals().get(base_name)

    # 3. Попробуй импортировать как модуль
    if obj is None:
        try:
            obj = importlib.import_module(base_name)
        except ImportError:
            return []  # Не найдено

    # Достаем вложенные атрибуты
    for attr in parts[1:]:
        try:
            obj = getattr(obj, attr)
        except AttributeError:
            return []  # Некорректный путь

    return dir(obj) if obj else []


def custom_key(s):
    # Заменяем символ _ на символ с очень высоким Unicode-кодом для сортировки
    return s.replace('_', chr(0x10FFFF)).lower()
