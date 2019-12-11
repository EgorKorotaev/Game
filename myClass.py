class Fact:
    def __init__(self):
        self.contents = ''
        self.status = False


class History:
    def __init__(self, fact=Fact()):
        self.fact = []
        self.status = False


class Diary:
    def __init__(self):
        self.write = []


class Inventory:
    def __init__(self):
        self.item = []


class Item:
    def __init__(self, contents='~', use='~', cost=0):
        self.contents = contents
        self.use = use
        self.cost = cost


class People:
    def __init__(self, nickname='Ник', name='фио', history=History(), inventory=Inventory()):
        self.nickname = nickname
        self.name = name
        self.history = history
        self.inventory = inventory


class Player(People):
    def __init__(self, diary, nickname, name, history, inventory):
        super().__init__(nickname, name, history, inventory)
        self.diary = diary


class NPC(People):
    def __init__(self, nickname, name, history, inventory):
        super().__init__(nickname, name, history, inventory)
        self.loyalty = 0

