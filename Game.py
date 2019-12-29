from Repository import Repository
from colorama import Fore, Back, Style
import os


class Game:

    def __init__(self):
        self.game_state = Repository.initial_game_state()  # в поле "состояние игры" записываем из хранилища
        self.player_choice = None
        # self.clear = lambda: os.system('clear')
        # начальнео состояние игры

    def game_loop(self):  # "игровой цикл". поле ввода вариантов действия
        print('Hello!')  # Означает начало игры

        while True:
            if self.player_choice == "0":  # если игрок выборал 0 - игра прекращается
                break
            self.display_dialogue()  # вызываем "отображение диалога"
            while True:
                self.player_choice = input()  # считываем выбор игрока
                try:  # вынести сообщения об ошибках в отдельную функцию
                    if self.player_choice == "0":  # если игрок выборал 0 - игра прекращается
                        break
                    elif self.player_choice == "raw_dialog":  # inventory TODO
                        pass
                    elif self.player_choice == "j":  # journal TODO
                        pass
                    else:
                        self.game_state.get_current_dialogue().make_choice(int(self.player_choice) - 1, self.game_state)
                        break
                        # у "состояния игры" в "получить текущем диалоге" "делаем выбор"
                        # и передаём парамет номер выбора и нынешнее состояние игры
                except IndexError:
                    print("Что-что? Такого варианта действия нет")
                except ValueError:
                    print("Не понимаю твоей команды, повтори")
        print('Goodbye!')  # конец игры

    def display_dialogue(self):  # "отображение диалога"
        dialogue = self.game_state.get_current_dialogue()  # в переменную диалог записываем "полученый текущий диалог"
        self.print_text(dialogue)
        for i, choice in enumerate(dialogue.list_choices(), 1):  # для каждого выбора из списка выборов
            print(Fore.LIGHTBLACK_EX + f'{i}|' + Style.RESET_ALL + choice.get_text())  # печатам текст выбора

    def print_text(self, dialogue):
        # self.clear()
        print(Fore.LIGHTBLACK_EX + '══════════════════════════════════════════════════' + Style.RESET_ALL)
        # print(Fore.LIGHTBLACK_EX + '🙡🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙢' + Style.RESET_ALL)
        # print(dialogue.get_text())  # печатаем на экране из текущего диалога "полученный текст"
        for char in dialogue.get_text():
            print(char, end="", flush=True)
            # time.sleep(0.04)
        # print(Fore.LIGHTBLACK_EX + '\n🙡🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙚🙛🙢' + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + '\n——————————————————————————————————————————————————' + Style.RESET_ALL)