# Вариант выбора, на примере можно видеть что может иметь любой побочный эффект, изменяя state
import Repository


class Choice:

    def __init__(self, text):
        self.text = text

    def apply(self, game_state):
        pass

    def get_text(self):
        return self.text


class SayPhrase(Choice):

    def __init__(self, text, dialogue_id):
        super().__init__(text)
        self.dialogue_id = dialogue_id

    def apply(self, game_state):
        game_state.change_dialogue(Repository.Repository.get_dialogue(self.dialogue_id))

    def get_text(self):
        return self.text


class GoToNpc(Choice):

    def __init__(self, npc):
        super().__init__(f'[{npc.get_name()}]')
        self.npc = npc

    def apply(self, game_state):
        game_state.change_dialogue(Repository.Repository.get_dialogue(self.npc.get_dialogue_id()))


class GoToOtherLocation(Choice):
    def __init__(self, location):
        super().__init__(f'[{location.get_name()}]')


class EndDialogue(Choice):

    def __init__(self, text):
        super().__init__(text)

    def apply(self, game_state):
        game_state.end_dialogue()

    def get_text(self):
        return self.text
