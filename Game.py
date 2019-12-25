import time

from Repository import Repository
from colorama import Fore, Back, Style


class Game:

    def __init__(self):
        self.game_state = Repository.initial_game_state()  # в поле "состояние игры" записываем из хранилища
        # начальнео состояние игры

    def game_loop(self):  # "игровой цикл". поле ввода вариантов действия
        print('Hello!')  # Означает начало игры

        while True:
            self.display_dialogue()  # вызываем "отображение диалога"
            player_choice = int(input())  # считываем выбор игрока
            if player_choice == 0:  # если игрок выборал 0 - игра прекращается
                break

            self.game_state.get_current_dialogue().make_choice(player_choice - 1, self.game_state)
        # у "состояния игры" в "получить текущем диалоге" "делаем выбор"
        # и передаём парамет номер выбора и нынешнее состояние игры
        print('Goodbye!')  # значает конец игры

    def display_dialogue(self):  # "отображение диалога"
        dialogue = self.game_state.get_current_dialogue()  # в переменную диалог записываем "полученый текущий диалог"
        self.print_text(dialogue)
        for i, choice in enumerate(dialogue.list_choices(), 1):  # для каждого выбора из списка выборов
            print(Fore.LIGHTBLACK_EX + f'{i}|' + Style.RESET_ALL + choice.get_text())  # печатам текст выбора

    def print_text(self, dialogue):
        print(Fore.LIGHTBLACK_EX + '🙡🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙢' + Style.RESET_ALL)
        # print(dialogue.get_text())  # печатаем на экране из текущего диалога "полученный текст"
        for char in dialogue.get_text():
            print(char, end="", flush=True)
            time.sleep(0.2)
        print(Fore.LIGHTBLACK_EX + '\n🙡🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙢' + Style.RESET_ALL)
