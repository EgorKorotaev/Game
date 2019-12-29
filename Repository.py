from __future__ import annotations
from Dialogue import Dialogue
from GameState import GameState
from Location import Location
from NPC import NPC
from Choice import SayPhrase, EndDialogue
import json


class Repository:
    data_dialogues = json.load(open(r'resources\dialogues.json', 'r', encoding="utf-8"))
    # data_map = json.load(open(r'resources\map.json', 'r', encoding="utf-8"))

    # rawDialogs = json.loads('resources\data.json')

    dialogues = {}

    # for raw_dialog in data_dialogues:
    #     print('****>', raw_dialog, '<****')
    #     dialogues[raw_dialog['key']] = raw_dialog
    #     print('!!!!>', dialogues[raw_dialog['key']], '<!!!!')

    dialog_keys = []
    for dialog in data_dialogues:
        dialog_keys.append(dialog['key'])

    for raw_dialog in data_dialogues:
        choices = []
        for choice in raw_dialog['dialogBranches']:
            if choice['nextDialogKey'] in dialog_keys:
                choices.append(SayPhrase(choice['branchName'], choice['nextDialogKey']))
            else:
                choices.append(EndDialogue('(В разработке)' + choice['branchName']))
        dialogues[raw_dialog['key']] = Dialogue(None, choices, raw_dialog['dialogText'])

    @staticmethod
    def get_dialogue(dialogue_id):  # "получить диалог" принимает "id диалога"
        return Repository.dialogues[dialogue_id]

    @staticmethod
    def get_location(id):
        # TODO AAA
        start = [
            NPC('start', '1')
        ]
        return Location(start, 'История первая: "Прототип движения по диалогам"')

    @staticmethod
    def initial_game_state():
        return GameState(Repository.get_location('start_location'))
