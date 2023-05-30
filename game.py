from ursina import Entity, Audio
import pickle

from object.map.map_chapter import MapChapter
from ui.scene.boardmenu import BoardMenu
from ui.scene.escapemenu import EscapeMenu
from ui.scene.mainmenu import MainMenu
from ui.component.info import Info


class Game(Entity):

    def __init__(self, player_name, menu=MainMenu):
        super().__init__()
        self.player = None

        self.load_player_data(player_name)
        self.menu = menu(game=self)

        self.ui = None
        self.chapter = None

    def load_player_data(self, player_name):
        try:
            with open(player_name + '.pickle', 'rb') as file:
                self.player = pickle.load(file)
        except FileNotFoundError:
            return None

    def save_player_data(self, player):
        with open(player.name + '.pickle', 'wb') as file:
            pickle.dump(player, file)
        self.load_player_data(player.name)

    def start_chapter(self, num=1):
        print(self.menu)
        self.menu.disable()
        # print(self.menu)
        # self.menu.disable()
        self.ui = Info(num)
        self.chapter = MapChapter(self.player, num)

    def open_board(self):
        self.ui.disable()
        self.menu = BoardMenu(self.player, self.ui.enable)

    def open_escape(self):
        self.ui.disable()
        self.menu = EscapeMenu(self.ui.enable, self.save_exit)

    def save_exit(self):
        self.save_player_data(player=self.player)
        print('save and exit')
        exit()

    def input(self, key):
        if key == 'q':
            self.open_board()
        elif key == 'escape':
            self.open_escape()
        elif key == 'space':
            import random
            a = Audio('aa', pitch=random.uniform(.5, 1), loop=True, autoplay=True)
