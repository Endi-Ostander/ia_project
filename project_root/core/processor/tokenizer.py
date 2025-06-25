import re
from typing import List
from core.common.utils import clean_text


class Tokenizer:
    def __init__(self):
        # Можно позже добавить список стоп-слов
        self.delimiters = r"[ \t\n\r\f\v.,!?;:\"()\-—]+"  # Разделители слов

    def tokenize(self, text: str) -> List[str]:
        """Разбивает строку на токены."""
        cleaned = clean_text(text)
        tokens = re.split(self.delimiters, cleaned)
        return [t for t in tokens if t]  # Убираем пустые строки

    def count_tokens(self, text: str) -> int:
        """Подсчитывает количество токенов."""
        return len(self.tokenize(text))

    def preview_tokens(self, text: str) -> None:
        """Выводит токены в консоль для отладки."""
        tokens = self.tokenize(text)
        print(f"[Tokenizer] → {tokens}")
