from game_logic import NumberGuessGame
from storage import ScoreStorage

def main():
    storage = ScoreStorage()
    user_id = "local_player"  # в боте будет tg user_id
    game = NumberGuessGame(user_id, storage)

    print("🎮 Добро пожаловать в игру 'Угадай число'!")
    print("Счёт будет сохраняться между играми.")
    print("Правила: угадай число от 1 до 100.")
    print("🎯 Точное попадание = +3, ближе чем на 5 = +1, иначе -1.\n")

    while True:
        try:
            guess = input("Введи число (или 'exit' для выхода): ")
            if guess.lower() == "exit":
                print("👋 Игра окончена. Твой финальный счёт:", storage.get_score(user_id))
                break

            guess = int(guess)
            result = game.guess(guess)
            print(result)
        except ValueError:
            print("⚠️ Введи число от 1 до 100 или 'exit'.")

if __name__ == "__main__":
    main()