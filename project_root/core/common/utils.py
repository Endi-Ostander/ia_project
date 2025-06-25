# core/common/utils.py

import json
import os
import re
import uuid
from datetime import datetime

def clean_text(text: str) -> str:
    """Удаляет лишние пробелы, спецсимволы и приводит к нижнему регистру."""
    text = re.sub(r'[^\w\s]', '', text)  # Удалить пунктуацию
    return re.sub(r'\s+', ' ', text).strip().lower()

def normalize_whitespace(text: str) -> str:
    """Приводит все пробелы к одному."""
    return re.sub(r'\s+', ' ', text).strip()

def generate_id() -> str:
    """Создаёт уникальный идентификатор."""
    return str(uuid.uuid4())

def timestamp() -> str:
    """Возвращает текущую дату и время в ISO формате."""
    return datetime.utcnow().isoformat()

def load_json(filepath: str) -> dict:
    """Загружает JSON-файл в словарь."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: dict) -> None:
    """Сохраняет словарь в JSON-файл."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def pretty_print(obj):
    """Удобный вывод словаря."""
    print(json.dumps(obj, indent=4, ensure_ascii=False))
