import json
import os

class ScoreStorage:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = self._load()

    def _load(self):
        """Загрузить сохранённые очки из файла"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = f.read().strip()
                    if not data:  # пустой файл
                        return {}
                    return json.loads(data)
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def _save(self):
        """Сохранить текущие очки в файл"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=4)

    def get_score(self, user_id: str) -> int:
        """Получить счёт игрока"""
        return self.scores.get(user_id, 0)

    def update_score(self, user_id: str, delta: int) -> int:
        """Обновить счёт игрока"""
        self.scores[user_id] = self.get_score(user_id) + delta
        self._save()
        return self.scores[user_id]

    def reset_score(self, user_id: str):
        """Сбросить счёт игрока"""
        self.scores[user_id] = 0
        self._save()




# import json
# import os

# class ScoreStorage:
#     def __init__(self, filename="scores.json"):
#         self.filename = filename
#         self.scores = self._load()

#     def _load(self):
#         """Загрузить сохранённые очки из файла"""
#         if os.path.exists(self.filename):
#             with open(self.filename, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         return {}

#     def _save(self):
#         """Сохранить текущие очки в файл"""
#         with open(self.filename, "w", encoding="utf-8") as f:
#             json.dump(self.scores, f, ensure_ascii=False, indent=4)

#     def get_score(self, user_id: str) -> int:
#         """Получить счёт игрока"""
#         return self.scores.get(user_id, 0)

#     def update_score(self, user_id: str, delta: int) -> int:
#         """Обновить счёт игрока"""
#         self.scores[user_id] = self.get_score(user_id) + delta
#         self._save()
#         return self.scores[user_id]

#     def reset_score(self, user_id: str):
#         """Сбросить счёт игрока"""
#         self.scores[user_id] = 0
#         self._save()