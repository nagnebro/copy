from ursina import Entity, Audio
import pickle

from object.map.map_chapter import MapChapter
from object.map.map_sprite import MapSprite
from ui.scene.boardmenu import BoardMenu
from ui.scene.escapemenu import EscapeMenu
from ui.scene.mainmenu import MainMenu
from ui.component.info import Info


class Game(Entity):

    def __init__(self, player_name, menu=MainMenu):
        super().__init__()
        self.player_data = None


        self.load_player_data(player_name)
        self.menu = menu(game=self)

        self.ui = None
        self.chapter = None

    def load_player_data(self, player_name):
        try:
            with open(player_name + '.pickle', 'rb') as file:
                self.player_data = pickle.load(file)
        except FileNotFoundError:
            return None

    def save_player_data(self, player_data):
        with open(player_data.name + '.pickle', 'wb') as file:
            pickle.dump(player_data, file)
        self.load_player_data(player_data.name)

    def start_chapter(self, num=1):
        print(self.menu)
        self.menu.disable()
        # print(self.menu)
        # self.menu.disable()
        self.ui = Info(num)
        # self.chapter = MapChapter(self.player_data, num)
        self.chapter = MapSprite(self.player_data, num)

    def open_board(self):
        self.ui.disable()
        print(type(self.player_data))
        self.menu = BoardMenu(self.player_data, self.ui.enable)

    def open_escape(self):
        self.ui.disable()
        self.menu = EscapeMenu(self.ui.enable, self.save_exit)

    def save_exit(self):
        self.save_player_data(player_data=self.player_data)
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
