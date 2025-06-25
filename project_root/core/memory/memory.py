import os
from typing import List, Optional
from core.common.utils import load_json, save_json, generate_id, timestamp
from core.common.types import Fact, KnowledgeEntry, KnowledgeType

MEMORY_FILE = "data/memory.json"
KNOWLEDGE_FILE = "data/knowledge_base.json"


class Memory:
    def __init__(self):
        self.facts = self._load_facts()
        self.knowledge = self._load_knowledge()

    def _load_facts(self) -> List[Fact]:
        data = load_json(MEMORY_FILE)
        return [Fact(**f) for f in data.get("facts", [])]

    def _load_knowledge(self) -> List[KnowledgeEntry]:
        data = load_json(KNOWLEDGE_FILE)
        return [KnowledgeEntry(**k) for k in data.get("entries", [])]

    def _save_facts(self):
        data = {"facts": [f.__dict__ for f in self.facts]}
        save_json(MEMORY_FILE, data)

    def _save_knowledge(self):
        data = {"entries": [k.__dict__ for k in self.knowledge]}
        save_json(KNOWLEDGE_FILE, data)

    def add_fact(self, subject: str, predicate: str, obj: str, source: Optional[str] = None):
        fact = Fact(
            id=generate_id(),
            subject=subject,
            predicate=predicate,
            obj=obj,
            source=source,
            timestamp=timestamp()
        )
        self.facts.append(fact)
        self._save_facts()

    def add_knowledge(self, title: str, content: str, k_type: KnowledgeType, tags: List[str]):
        entry = KnowledgeEntry(
            id=generate_id(),
            title=title,
            content=content,
            type=k_type,
            tags=tags,
            created=timestamp()
        )
        self.knowledge.append(entry)
        self._save_knowledge()

    def find_facts_by_subject(self, subject: str) -> List[Fact]:
        return [f for f in self.facts if f.subject == subject]

    def find_knowledge_by_tag(self, tag: str) -> List[KnowledgeEntry]:
        return [k for k in self.knowledge if tag in k.tags]
