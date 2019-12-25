from __future__ import annotations
from Dialogue import Dialogue
from GameState import GameState
from Location import Location
from NPC import NPC
from Choice import SayPhrase, EndDialogue
import json


class Repository:
    # должно загружаться из базы данных
    dialogues = {}
    # dialogues = {
    #     'hren_dialogue1': Dialogue(None, [
    #         SayPhrase('Это точно?', 'hren_dialogue2'),
    #         EndDialogue('Пока')
    #     ], 'Привет, я хрен с горы.'),
    #
    #     'hren_dialogue2': Dialogue(None, [EndDialogue('Ну теперь точно пока.')], 'Абсолютно!.'),
    #
    #     'lady_dialogue1': Dialogue(None, [
    #         SayPhrase('Привет, красотка', 'lady_dialogue2'),
    #         SayPhrase('Добрый день, мисс.', 'lady_dialogue3'),
    #         EndDialogue('До свидания.')
    #     ], 'Девушка молчаливо смотрит на вас.'),
    #
    #     'lady_dialogue2': Dialogue(None, [EndDialogue('Уйти.')], 'Она брезгливо отворачивается.'),
    #
    #     'lady_dialogue3': Dialogue(None, [
    #         SayPhrase('Не хотите что-нибудь выпить в этом прекрасном заведении через дорогу.', 'lady_dialogue2'),
    #         EndDialogue('Уйти.')
    #     ], 'Здравствуйте, я Имя.'),
    # }
    data = json.load(open(r'resources\map.json', 'r', encoding="utf-8"))

    for i in data:
        # print('*1', i)
        choices = []
        for j in data[i][0]:
            # print('*2', j, type(j))
            if j != 0:
                choices.append(SayPhrase(j[0], j[1]))
            else:
                choices.append(EndDialogue("Далее"))
        dialogues[i] = Dialogue(None, choices, data[i][1])

    @staticmethod
    def get_dialogue(dialogue_id):  # "получить диалог" принимает "id диалога"
        return Repository.dialogues[dialogue_id]

    @staticmethod
    def get_location(id):
        # TODO AAA
        # npc_HARDCODED = [
        #     NPC('Хрен с горы', 'hren_dialogue1'),
        #     NPC('Таинственная леди', 'lady_dialogue1')
        # ]
        # return Location(npc_HARDCODED, 'Вы стоите посреди селения "Артихан"')
        start = [
            NPC('start', '1')
        ]
        return Location(start, 'История первая: "Прототип движения по диалогам"')

    @staticmethod
    def initial_game_state():
        return GameState(Repository.get_location('start_location'))
