class GameState:

    def __init__(self, location):
        self.current_location = location
        self.current_dialogue = location.get_dialogue()

    def change_dialogue(self, dialogue):
        self.current_dialogue = dialogue

    def end_dialogue(self):
        self.current_dialogue = self.current_location.get_dialogue()

    def get_current_dialogue(self):
        return self.current_dialogue
