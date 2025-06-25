# core/learner/rules.py

from typing import List, Optional, Dict, Any
from core.common.types import PhraseType

class Rule:
    """
    Правило для интерпретации фразы и преобразования в знание или действие.
    """
    def __init__(self, name: str, condition: callable, action: callable):
        self.name = name
        self.condition = condition  # Функция: принимает текст или токены, возвращает bool
        self.action = action        # Функция: принимает текст или токены, возвращает результат


class RulesEngine:
    def __init__(self):
        self.rules: List[Rule] = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def apply_rules(self, phrase_type: PhraseType, tokens: List[str], raw_text: str) -> Optional[Dict[str, Any]]:
        """
        Применяет правила к фразе. Возвращает результат первого применимого правила.
        """
        for rule in self.rules:
            if rule.condition(phrase_type, tokens, raw_text):
                return rule.action(phrase_type, tokens, raw_text)
        return None


# Пример условий и действий:

def condition_fact(phrase_type: PhraseType, tokens: List[str], raw_text: str) -> bool:
    # Условие: утверждение с минимум 3 токенами
    return phrase_type == PhraseType.STATEMENT and len(tokens) >= 3

def action_fact(phrase_type: PhraseType, tokens: List[str], raw_text: str) -> Dict[str, Any]:
    # Действие: преобразовать в факт (subject, predicate, object)
    subject = tokens[0]
    predicate = tokens[1]
    obj = " ".join(tokens[2:])
    return {"type": "fact", "subject": subject, "predicate": predicate, "object": obj, "source": raw_text}

# Инициализация движка и добавление правила
rules_engine = RulesEngine()
rules_engine.add_rule(Rule("fact_rule", condition_fact, action_fact))
