class Dialogue:

    def __init__(self, parent, choices, text):
        self.text = text
        self.parent = parent
        self.choices = choices
        self.visited_marks = [False] * len(self.choices)

    def make_choice(self, idx, game_state):
        self.visited_marks[idx] = True
        return self.choices[idx].apply(game_state)

    def get_text(self):
        return self.text

    def list_choices(self):
        return self.choices
