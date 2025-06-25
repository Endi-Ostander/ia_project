# core/processor/classifier.py

from core.common.types import PhraseType


class Classifier:
    def __init__(self):
        self.question_starters = {"что", "кто", "где", "почему", "зачем", "как", "когда", "сколько", "можно", "ли"}
        self.command_verbs = {"расскажи", "покажи", "скажи", "объясни", "запомни", "ответь", "найди"}

    def classify(self, text: str) -> PhraseType:
        lowered = text.strip().lower()

        if lowered.endswith("?"):
            return PhraseType.QUESTION

        if any(lowered.startswith(q) for q in self.question_starters):
            return PhraseType.QUESTION

        if any(lowered.startswith(cmd) for cmd in self.command_verbs):
            return PhraseType.COMMAND

        if lowered.endswith(".") or " " in lowered:
            return PhraseType.STATEMENT

        return PhraseType.UNKNOWN
