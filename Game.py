from Repository import Repository


class Game:

    def __init__(self):
        self.game_state = Repository.initial_game_state()

    def game_loop(self):
        print('Hello!')

        while True:
            self.display_dialogue()
            player_choice = int(input())
            if player_choice == 0:
                break

            self.game_state.get_current_dialogue().make_choice(player_choice - 1, self.game_state)

        print('Goodbye!')

    def display_dialogue(self):
        dialogue = self.game_state.get_current_dialogue()
        print(dialogue.get_text())
        for i, choice in enumerate(dialogue.list_choices(), 1):
            print(f'{i}. ', choice.get_text())
