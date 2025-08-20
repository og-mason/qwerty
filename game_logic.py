import random
from storage import ScoreStorage

class NumberGuessGame:
    def __init__(self, user_id: str, storage: ScoreStorage):
        self.user_id = user_id
        self.storage = storage
        self.target = random.randint(1, 100)

    def reset(self):
        self.target = random.randint(1, 100)

    def guess(self, number: int) -> str:
        if not (1 <= number <= 100):
            return "Число должно быть от 1 до 100!"

        diff = abs(number - self.target)

        if diff == 0:
            new_score = self.storage.update_score(self.user_id, 3)
            result = f"🎯 Точно! Ты угадал число {self.target}. +3 очка!"
        elif diff <= 5:
            new_score = self.storage.update_score(self.user_id, 1)
            result = f"👍 Почти! Ты был близок к {self.target}. +1 очко!"
        else:
            new_score = self.storage.update_score(self.user_id, -1)
            result = f"❌ Не угадал. Загаданное число было {self.target}. -1 очко."

        self.reset()
        return result + f"\nТекущий счёт: {new_score}"