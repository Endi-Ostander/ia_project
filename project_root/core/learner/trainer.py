# core/learner/trainer.py

from core.processor.tokenizer import Tokenizer
from core.processor.classifier import Classifier
from core.memory.memory import Memory
from core.common.types import PhraseType
from core.learner.rules import RulesEngine  # Импортируем движок правил


class Trainer:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.classifier = Classifier()
        self.memory = Memory()
        self.rules_engine = RulesEngine()

    def process_text(self, text: str):
        """Главная точка обучения: обработка входного текста"""
        phrase_type = self.classifier.classify(text)
        tokens = self.tokenizer.tokenize(text)

        print(f"[Trainer] Тип фразы: {phrase_type.name}")
        print(f"[Trainer] Токены: {tokens}")

        # Применяем правила к входным данным
        rule_results = self.rules_engine.apply_rules(phrase_type, tokens, text)

        if rule_results.get("add_fact"):
            fact = rule_results["add_fact"]
            self.memory.add_fact(
                subject=fact.get("subject"),
                predicate=fact.get("predicate"),
                obj=fact.get("obj"),
                source=text
            )
            print(f"[Trainer] Запомнено через правила: {fact.get('subject')} — {fact.get('predicate')} — {fact.get('obj')}")
        else:
            # Если правило не сработало, базовое обучение на утверждении
            if phrase_type == PhraseType.STATEMENT:
                self._learn_fact(tokens, source=text)
            elif phrase_type == PhraseType.QUESTION:
                print("[Trainer] Это вопрос — пока не обучаемся, только классификация.")
            elif phrase_type == PhraseType.COMMAND:
                print("[Trainer] Команда — здесь будет логика исполнения.")
            else:
                print("[Trainer] Не удалось определить тип фразы.")

    def _learn_fact(self, tokens, source: str):
        """Простое обучение на утверждении (если правила не применились)"""
        if len(tokens) < 3:
            print("[Trainer] Недостаточно информации для факта.")
            return

        subject = tokens[0]
        predicate = tokens[1]
        obj = " ".join(tokens[2:])

        self.memory.add_fact(subject, predicate, obj, source=source)
        print(f"[Trainer] Запомнено: {subject} — {predicate} — {obj}")
