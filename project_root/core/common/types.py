from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any, Optional


class PhraseType(Enum):
    """Типы фраз, которые может обрабатывать ИИ."""
    STATEMENT = "statement"    # Утверждение
    QUESTION = "question"      # Вопрос
    COMMAND = "command"        # Команда
    UNKNOWN = "unknown"        # Неопределено


class KnowledgeType(Enum):
    """Типы знаний, сохраняемых в память."""
    FACT = "fact"
    CONCEPT = "concept"
    DEFINITION = "definition"
    RULE = "rule"
    EVENT = "event"


@dataclass
class Phrase:
    """Структура входной фразы."""
    text: str
    tokens: List[str]
    phrase_type: PhraseType
    intent: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class Fact:
    """Факт, который можно сохранить в память."""
    id: str
    subject: str
    predicate: str
    obj: str
    source: Optional[str]
    timestamp: str


@dataclass
class KnowledgeEntry:
    """Хранилище произвольной информации."""
    id: str
    title: str
    content: str
    type: KnowledgeType
    tags: List[str]
    created: str
