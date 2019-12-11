from Choice import GoToNpc
from Dialogue import Dialogue


class Location:

    def __init__(self, npc_list, text):
        self.npc_list = npc_list
        choices = []
        for npc in npc_list:
            choices.append(GoToNpc(npc))

        self.dialogue = Dialogue(None, choices, text)

    def get_dialogue(self):
        return self.dialogue
